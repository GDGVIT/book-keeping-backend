from django.conf import settings
from django.urls import include, re_path
from rest_framework.routers import DefaultRouter
from rest_framework.routers import SimpleRouter

from bookeeping.users.api.views import UserViewSet

router = DefaultRouter() if settings.DEBUG else SimpleRouter()

router.register("users", UserViewSet)

urlpatterns = [
    re_path("users/", include("bookeeping.users.api.urls")),
    re_path("core/", include("bookeeping.core.api.urls")),
]

app_name = "api"
urlpatterns += router.urls
