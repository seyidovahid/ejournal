from .models import (
    Faculty,
    Department,
    Subject,
    StudentProfile,
    TeacherProfile,
    Major,
    StudentGroup,
    Lesson,
    LessonMaterial,
)
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

# Unregister the built-in User model admin
admin.site.unregister(User)


# Register the custom User model admin
@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display = (
        "username",
        "id",
        "email",
        "first_name",
        "last_name",
        "is_staff",
        "is_active",
    )


@admin.register(Faculty)
class FacultyAdmin(admin.ModelAdmin):
    list_display = ["name"]


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ["name", "faculty"]


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ["name", "code", "department"]


@admin.register(StudentProfile)
class StudentAdmin(admin.ModelAdmin):
    list_display = ["user"]


@admin.register(TeacherProfile)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ["get_full_name", "department"]


@admin.register(Major)
class MajorAdmin(admin.ModelAdmin):
    list_display = ["name", "level", "code", "faculty"]


@admin.register(StudentGroup)
class StudentGroupAdmin(admin.ModelAdmin):
    list_display = ["name", "major"]


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = [
        "subject",
        "teacher",
        "topic",
        "lesson_type",
        "date",
        "start_time",
        "end_time",
    ]


@admin.register(LessonMaterial)
class LessonMaterialAdmin(admin.ModelAdmin):
    list_display = ["name", "file", "lesson"]

    # def get_lessons(self, obj):
    #     return ", ".join([lesson.subject.name for lesson in obj.lesson.all()])

    # get_lessons.short_description = "Lessons"
