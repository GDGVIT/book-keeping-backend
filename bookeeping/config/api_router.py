from django.conf import settings
from django.urls import include, re_path, path
from rest_framework.routers import DefaultRouter
from rest_framework.routers import SimpleRouter

from bookeeping.users.api.views import UserViewSet

router = DefaultRouter() if settings.DEBUG else SimpleRouter()

router.register("users", UserViewSet)

urlpatterns = [
    path("users/", include("bookeeping.users.api.urls")),
    re_path("api/", include("bookeeping.core.api.urls")),
]
app_name = "api"
urlpatterns = router.urls
