from django.contrib.auth.models import User
from rest_framework import serializers
from .models import TeacherProfile, StudentProfile
from django.forms.models import model_to_dict


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("username", "password", "email")


class TeacherProfileSerializer(serializers.ModelSerializer):
    # user = UserSerializer()

    class Meta:
        model = TeacherProfile
        fields = ("user", "faculty", "qualifications", "teaching_experience")

    def create(self, validated_data):
        # user_data = validated_data.pop("user")
        # user = User.objects.create(**user_data)
        # user.set_password(user_data["password"])
        # user.save()

        # GET USER WITH ID
        # uid = validated_data.pop("user")

        # user = User.objects.get(pk=uid)

        # print("The User:", model_to_dict(user))

        teacher_profile = TeacherProfile.objects.create(**validated_data)
        return teacher_profile


class StudentProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = StudentProfile
        fields = ("user", "additional_fields")

    def create(self, validated_data):
        user_data = validated_data.pop("user")
        user = User.objects.create(**user_data)
        user.set_password(user_data["password"])
        user.save()
        student_profile = StudentProfile.objects.create(user=user, **validated_data)
        return student_profile
