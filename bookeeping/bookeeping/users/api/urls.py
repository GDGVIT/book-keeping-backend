from django.urls import path
from rest_framework.routers import DefaultRouter
from bookeeping.users.api.views import (
    RegistrationView,
    LoginRegistrationView,
)
from rest_framework_simplejwt.views import TokenRefreshView

app_name = "users"

urlpatterns = [
    path("register/", RegistrationView.as_view(), name="register"),
    path("login/", LoginRegistrationView.as_view(), name="login"),
    path("refresh_token/", TokenRefreshView.as_view(), name="refresh_token"),
]