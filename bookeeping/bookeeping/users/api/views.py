from http import HTTPStatus
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.mixins import ListModelMixin
from rest_framework.mixins import RetrieveModelMixin
from rest_framework.mixins import UpdateModelMixin
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import get_user_model


from bookeeping.users.models import User

from .serializers import UserSerializer, UserLoginSerializer


class UserViewSet(RetrieveModelMixin, ListModelMixin, UpdateModelMixin, GenericViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    lookup_field = "pk"

    def get_queryset(self, *args, **kwargs):
        assert isinstance(self.request.user.id, int)
        return self.queryset.filter(id=self.request.user.id)

    @action(detail=False)
    def me(self, request):
        serializer = UserSerializer(request.user, context={"request": request})
        return Response(status=status.HTTP_200_OK, data=serializer.data)

User = get_user_model()

class RegistrationView(APIView):
    permission_classes = [AllowAny]
    authentication_classes = []

    @staticmethod
    def post(request):
        name = request.data.get("name", None)
        email = request.data.get("email", None)
        password = request.data.get("password", None)

        if any([name, email, password]) is None:
            return Response(
                {"detail": "Please fill in all the fields!"},
                status=HTTPStatus.BAD_REQUEST,
            )
            
        user = User.objects.create_user(
            name=name,
            email=email,
            password=password,
        )
        
        return Response(
            {"detail":"User created successfully"},
            status=HTTPStatus.CREATED,
        )

class LoginRegistrationView(APIView):
    permission_classes = []
    authentication_classes = []

    @staticmethod
    def post(request):
        name= request.data.get("name")
        email = request.data.get("email")
        password = request.data.get("password")

        if not email or not password:
            return Response(
                {"detail": "Email and password are required."},
                status=HTTPStatus.BAD_REQUEST,
            )
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            user = User.objects.create_user(
            name=name,
            email=email,
            password=password,
            )
            refresh_token = RefreshToken.for_user(user)
            serializer = UserLoginSerializer(user)
            serializer.access_token = refresh_token.access_token
            serializer.refresh_token = str(refresh_token)

            return Response(
                {
                    "data": serializer.data,
                    "access_token": str(refresh_token.access_token),
                    "refresh_token": str(refresh_token),
                },
                status=HTTPStatus.OK,
            )

        if not user.check_password(password):
            return Response({"detail": "Incorrect password."}, status=HTTPStatus.BAD_REQUEST)

            # Generate JWT refresh token for the user
        refresh_token = RefreshToken.for_user(user)

        serializer = UserLoginSerializer(user)
        serializer.access_token = refresh_token.access_token
        serializer.refresh_token = str(refresh_token)

        return Response(
            {
                "data": serializer.data,
                "access_token": str(refresh_token.access_token),
                "refresh_token": str(refresh_token),
            },
            status=HTTPStatus.OK,
        )
        



