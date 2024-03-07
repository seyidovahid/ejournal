from django.contrib.auth.models import User
from django.db import models


class Faculty(models.Model):
    name = models.CharField(max_length=255)
    department = models.ForeignKey(
        "Department", on_delete=models.CASCADE, related_name="faculties", null=True
    )

    def __str__(self) -> str:
        return self.name


class Department(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name


class Subject(models.Model):
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=10, unique=True)
    description = models.TextField(blank=True)
    prerequisite_subjects = models.ManyToManyField("self", blank=True)

    def __str__(self) -> str:
        return self.name


class Major(models.Model):
    name = models.CharField(max_length=255)
    department = models.ForeignKey("Department", on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name


class AbstractUserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    class Meta:
        abstract = True


class StudentProfile(AbstractUserProfile):
    major = models.ForeignKey("Major", on_delete=models.CASCADE)
    enrollment_date = models.DateField(auto_now_add=True)


class TeacherProfile(AbstractUserProfile):
    faculty = models.ForeignKey("Faculty", on_delete=models.CASCADE)
    qualifications = models.TextField(blank=True)
    teaching_experience = models.TextField(blank=True)
