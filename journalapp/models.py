from django.contrib.auth.models import User
from django.db import models

LEVEL_CHOICES = (
    ("Masters", "Masters"),
    ("Bachelor", "Bachelor"),
)

GENDER_CHOICES = (
    ("Male", "Male"),
    ("Female", "Female"),
)

LESSON_TYPES = (
    ("Lecture", "Mühazirə"),
    ("Practice", "Seminar"),
    ("Laboratory", "Laboratoriya"),
)


class Faculty(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name


class Department(models.Model):
    name = models.CharField(max_length=255)
    faculty = models.ForeignKey("Faculty", on_delete=models.PROTECT)
    description = models.TextField(blank=True)

    def __str__(self) -> str:
        return self.name


class Subject(models.Model):
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=10, unique=True)
    description = models.TextField(blank=True)
    department = models.ForeignKey("Department", on_delete=models.PROTECT)

    def __str__(self) -> str:
        return self.name


class Major(models.Model):
    level = models.CharField(max_length=255, choices=LEVEL_CHOICES)
    code = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=255)
    faculty = models.ForeignKey("Faculty", on_delete=models.PROTECT)

    def __str__(self) -> str:
        return self.name


class AbstractUserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=20, blank=True)
    address = models.CharField(max_length=255, blank=True)
    date_of_birth = models.DateField(blank=True, null=True)
    gender = models.CharField(max_length=20, choices=GENDER_CHOICES, blank=True)

    def __str__(self) -> str:
        return self.user.first_name + " " + self.user.last_name

    def get_full_name(self):
        return self.user.first_name + " " + self.user.last_name

    class Meta:
        abstract = True


class StudentProfile(AbstractUserProfile):
    group = models.ForeignKey("StudentGroup", on_delete=models.PROTECT)


class TeacherProfile(AbstractUserProfile):
    department = models.ForeignKey("Department", on_delete=models.PROTECT)


class StudentGroup(models.Model):
    name = models.CharField(max_length=255)
    major = models.ForeignKey("Major", on_delete=models.PROTECT)

    def __str__(self) -> str:
        return self.name


class Lesson(models.Model):
    student_group = models.ManyToManyField("StudentGroup")
    teacher = models.ForeignKey("TeacherProfile", on_delete=models.SET_NULL, null=True)
    subject = models.ForeignKey("Subject", on_delete=models.PROTECT)
    topic = models.CharField(max_length=255)
    lesson_type = models.CharField(max_length=255, choices=LESSON_TYPES)
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self) -> str:
        return f"{self.subject} - {self.date}"


class LessonMaterial(models.Model):
    lesson = models.ForeignKey("Lesson", on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=255)
    file = models.FileField(upload_to="lesson_materials")

    def __str__(self) -> str:
        return self.name
