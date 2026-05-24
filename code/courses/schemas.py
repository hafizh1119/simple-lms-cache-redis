from ninja import Schema
from typing import Optional, List
from datetime import datetime


class RegisterIn(Schema):
    username: str
    email: str
    password: str
    first_name: Optional[str] = ""
    last_name: Optional[str] = ""
    role: Optional[str] = "student"


class LoginIn(Schema):
    username: str
    password: str


class RefreshIn(Schema):
    refresh: str


class TokenOut(Schema):
    access: str
    refresh: str


class UserOut(Schema):
    id: int
    username: str
    email: str
    first_name: str
    last_name: str
    role: str


class ProfileUpdateIn(Schema):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    email: Optional[str] = None


class CourseIn(Schema):
    name: str
    description: Optional[str] = "-"
    price: Optional[int] = 10000


class CoursePatchIn(Schema):
    name: Optional[str] = None
    description: Optional[str] = None
    price: Optional[int] = None


class CourseOut(Schema):
    id: int
    name: str
    description: str
    price: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


class CourseListOut(Schema):
    count: int
    results: List[CourseOut]


class EnrollmentIn(Schema):
    course_id: int


class ProgressIn(Schema):
    content_id: int


class CourseMemberOut(Schema):
    id: int
    course_id: CourseOut  
    roles: str

    class Config:
        from_attributes = True


class CourseContentCompletionOut(Schema):
    id: int
    member_id: int      
    content_id: int    
    completed: bool
    completed_at: datetime

    class Config:
        from_attributes = True

    @staticmethod
    def resolve_member_id(obj):
        return obj.member_id_id  

    @staticmethod
    def resolve_content_id(obj):
        return obj.content_id_id

# Tambah schema Teacher (nested di CourseOut)
class TeacherOut(Schema):
    id: int
    username: str
    full_name: str

    class Config:
        from_attributes = True

    @staticmethod
    def resolve_full_name(obj):
        return f"{obj.first_name} {obj.last_name}".strip()


# Update CourseOut — tambah field teacher
class CourseOut(Schema):
    id: int
    name: str
    description: str
    price: int
    teacher: TeacherOut  # ← tambah ini
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


# Update CourseMemberOut — tambah user_id
class CourseMemberOut(Schema):
    id: int
    course_id: CourseOut
    user_id: int        # ← tambah ini
    roles: str

    class Config:
        from_attributes = True

    @staticmethod
    def resolve_user_id(obj):
        return obj.user_id_id  # ← karena ForeignKey namanya user_id


# Tambah CourseContentOut
class CourseContentOut(Schema):
    id: int
    name: str
    description: str
    video_url: Optional[str] = None
    course_id: int

    class Config:
        from_attributes = True

    @staticmethod
    def resolve_course_id(obj):
        return obj.course_id_id


# Update CourseContentCompletionOut — perbaiki resolve
class CourseContentCompletionOut(Schema):
    id: int
    member_id: int
    content_id: int
    completed: bool
    completed_at: datetime

    class Config:
        from_attributes = True

    @staticmethod
    def resolve_member_id(obj):
        return obj.member_id_id

    @staticmethod
    def resolve_content_id(obj):
        return obj.content_id_id  