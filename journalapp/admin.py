from .models import Faculty, Department, Subject, StudentProfile, TeacherProfile, Major
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
    list_display = ["id", "name", "department"]


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ["name"]


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ["name", "code", "description"]


@admin.register(StudentProfile)
class StudentAdmin(admin.ModelAdmin):
    list_display = ["user", "major", "enrollment_date"]


@admin.register(TeacherProfile)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ["user", "faculty", "qualifications", "teaching_experience"]


@admin.register(Major)
class MajorAdmin(admin.ModelAdmin):
    list_display = ["name", "department"]
