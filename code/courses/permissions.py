from ninja.errors import HttpError


def get_role(user):
    if user.is_superuser:
        return "admin"

    if user.groups.filter(name="instructor").exists():
        return "instructor"

    return "student"


def is_admin(user):
    if get_role(user) != "admin":
        raise HttpError(403, "Admin only")


def is_instructor(user):
    if get_role(user) not in ["instructor", "admin"]:
        raise HttpError(403, "Instructor only")


def is_student(user):
    if not user.is_authenticated:
        raise HttpError(401, "Login required")


def is_course_owner(user, course):
    if course.teacher_id != user.id and get_role(user) != "admin":
        raise HttpError(403, "Not course owner")