from django.utils import timezone
from django.core.mail import send_mail
from rest_framework.views import APIView, Response, status
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

from bookeeping.core.models import Business, Items, Inventory, Invoices, Parties, Transactions
from bookeeping.core.api.serializers import BusinessSerializer, ItemsSerializer, InventorySerializer, InvoicesSerializer, PartiesSerializer, TransactionsSerializer

class BusinessViewSet(ModelViewSet):
    queryset = Business.objects.all()
    serializer_class = BusinessSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

class ItemsViewSet(ModelViewSet):
    queryset = Items.objects.all()
    serializer_class = ItemsSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

class InventoryViewSet(ModelViewSet):
    queryset = Inventory.objects.all()
    serializer_class = InventorySerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

class InvoicesViewSet(ModelViewSet):
    queryset = Invoices.objects.all()
    serializer_class = InvoicesSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

class PartiesViewSet(ModelViewSet):
    queryset = Parties.objects.all()
    serializer_class = PartiesSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

class TransactionsViewSet(ModelViewSet):
    queryset = Transactions.objects.all()
    serializer_class = TransactionsSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

