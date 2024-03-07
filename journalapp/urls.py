from django.urls import path
from .views import UserProfileView, CreateUserView, UserLoginAPIView

urlpatterns = [
    path("create_profile/", UserProfileView.as_view(), name="create_profile"),
    path("create_user/", CreateUserView.as_view(), name="create_user"),
    path("login/", UserLoginAPIView.as_view(), name="login"),
]
