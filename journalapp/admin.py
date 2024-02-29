from django.contrib import admin
from .models import Faculty, Department, Subject, Student, Teacher, Major


@admin.register(Faculty)
class FacultyAdmin(admin.ModelAdmin):
    list_display = ["name", "department"]


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ["name"]


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ["name", "code", "description"]


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ["user", "major", "enrollment_date"]


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ["user", "faculty", "qualifications", "teaching_experience"]


@admin.register(Major)
class MajorAdmin(admin.ModelAdmin):
    list_display = ["name", "department"]
