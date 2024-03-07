from rest_framework import status, views, permissions, generics
from django.contrib.auth.models import User
from rest_framework.response import Response
from .serializers import (
    TeacherProfileSerializer,
    StudentProfileSerializer,
    UserSerializer,
)
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from django.contrib.auth import authenticate


class UserProfileView(views.APIView):
    def post(self, request, *args, **kwargs):
        profile_type = request.data.get("profile_type")
        if profile_type == "teacher":
            serializer = TeacherProfileSerializer(data=request.data)
        elif profile_type == "student":
            serializer = StudentProfileSerializer(data=request.data)
        else:
            return Response(
                {"error": "Invalid profile type"}, status=status.HTTP_400_BAD_REQUEST
            )

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    permission_classes = [permissions.AllowAny]


# class UserProfileView(generics.CreateAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer


class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserLoginAPIView(views.APIView):
    permission_classes = [permissions.AllowAny]
    authentication_classes = [TokenAuthentication]

    def post(self, request, *args, **kwargs):
        username = request.data.get("username")
        password = request.data.get("password")
        print(
            "this is the user:",
            {
                "username": username,
                "password": password,
            },
        )
        user = authenticate(username=username, password=password)
        if user:
            token, created = Token.objects.get_or_create(user=user)
            return Response({"token": token.key}, status=status.HTTP_200_OK)
        return Response({"error": "some error"}, status=status.HTTP_401_UNAUTHORIZED)
