from typing import Optional
from django.contrib.auth import authenticate
from django.contrib.auth.models import User, Group
from ninja import NinjaAPI
from ninja.errors import HttpError
from django.core.cache import cache
import time

from courses.models import Course, CourseMember, CourseContent, CourseContentCompletion
from courses.schemas import *
from courses.auth import auth, create_token, decode_token
from courses.permissions import *
from courses.helpers import get_object_or_404

api = NinjaAPI(
    title="Simple LMS API",
    version="1.0.0",
)


# ================= USER HELPER =================

def user_dict(user):
    return {
        "id": user.id,
        "username": user.username,
        "email": user.email,
        "first_name": user.first_name,
        "last_name": user.last_name,
        "role": get_role(user),
    }


# ================= AUTH =================

@api.post("/auth/register")
def register(request, data: RegisterIn):
    if User.objects.filter(username=data.username).exists():
        raise HttpError(400, "Username used")

    user = User.objects.create_user(
        username=data.username,
        email=data.email,
        password=data.password,
        first_name=data.first_name,
        last_name=data.last_name,
    )

    group, _ = Group.objects.get_or_create(name=data.role)
    user.groups.add(group)

    return user_dict(user)


@api.post("/auth/login")
def login(request, data: LoginIn):
    user = authenticate(username=data.username, password=data.password)

    if not user:
        raise HttpError(401, "Login gagal")

    return {
        "access": create_token(user),
        "refresh": create_token(user, "refresh"),
    }


@api.post("/auth/refresh")
def refresh_token(request, data: RefreshIn):
    payload = decode_token(data.refresh)
    user = get_object_or_404(User, id=payload["user_id"])

    return {
        "access": create_token(user),
        "refresh": create_token(user, "refresh"),
    }


@api.get("/auth/me", auth=auth)
def me(request):
    return user_dict(request.auth)


@api.put("/auth/me", auth=auth)
def update_me(request, data: ProfileUpdateIn):
    user = request.auth

    if data.first_name is not None:
        user.first_name = data.first_name
    if data.last_name is not None:
        user.last_name = data.last_name
    if data.email is not None:
        user.email = data.email

    user.save()
    return user_dict(user)


# ================= COURSES =================

@api.get("/courses")
def list_courses(request, search: Optional[str] = None):

    cache_key = f"courses_list:{search}"

    # =====================================
    # CHECK CACHE REDIS
    # =====================================
    cached_data = cache.get(cache_key)

    if cached_data is not None:
        print("Data diambil dari CACHE Redis")
        return cached_data

    # =====================================
    # CACHE MISS
    # =====================================
    print("Data diambil dari DATABASE")

    # simulasi query lambat
    time.sleep(2)

    qs = Course.objects.all()

    if search:
        qs = qs.filter(name__icontains=search)

    result = {
        "count": qs.count(),
        "results": [CourseOut.from_orm(c) for c in qs],
    }

    # =====================================
    # SAVE TO CACHE
    # =====================================
    cache.set(cache_key, result, timeout=300)

    return result

@api.get("/courses/{id}")
def detail_course(request, id: int):
    course = get_object_or_404(Course, id=id)
    return CourseOut.from_orm(course)


@api.post("/courses", auth=auth)
def create_course(request, data: CourseIn):

    is_instructor(request.auth)

    course = Course.objects.create(
        name=data.name,
        description=data.description,
        price=data.price,
        teacher=request.auth,
    )

    # hapus cache courses
    cache.delete_pattern("courses_list:*")

    return CourseOut.from_orm(course)


@api.patch("/courses/{id}", auth=auth)
def update_course(request, id: int, data: CoursePatchIn):
    course = get_object_or_404(Course, id=id)
    is_course_owner(request.auth, course)

    if data.name:
        course.name = data.name
    if data.description:
        course.description = data.description
    if data.price:
        course.price = data.price

    course.save()

    cache.delete_pattern("courses_list:*")
    cache.delete(f"course_detail:{id}")

    return CourseOut.from_orm(course)


@api.delete("/courses/{id}", auth=auth)
def delete_course(request, id: int):
    is_admin(request.auth)

    course = get_object_or_404(Course, id=id)
    course.delete()

    cache.delete_pattern("courses_list:*")
    cache.delete(f"course_detail:{id}")

    return {"success": True}


# ================= ENROLLMENTS =================

@api.post("/enrollments", auth=auth)
def enroll(request, data: EnrollmentIn):
    is_student(request.auth)

    course = get_object_or_404(Course, id=data.course_id)

    if CourseMember.objects.filter(course_id=course, user_id=request.auth).exists():
        raise HttpError(400, "Sudah enroll")

    member = CourseMember.objects.create(
        course_id=course,
        user_id=request.auth,
        roles="std",
    )

    return CourseMemberOut.from_orm(member)


@api.get("/enrollments/my-courses", auth=auth)
def my_courses(request):
    members = CourseMember.objects.filter(user_id=request.auth)
    return [CourseMemberOut.from_orm(m) for m in members]


@api.post("/enrollments/{id}/progress", auth=auth)
def progress(request, id: int, data: ProgressIn):
    member = get_object_or_404(CourseMember, id=id)
    content = get_object_or_404(CourseContent, id=data.content_id)

    completion = CourseContentCompletion.objects.create(
        member_id=member,
        content_id=content,
    )
    return CourseContentCompletionOut.from_orm(completion)