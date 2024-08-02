from django.utils import timezone
from django.core.mail import send_mail
from rest_framework.views import APIView, Response, status
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

from bookeeping.core.models import Business, Items, Inventory, Invoices, Parties, Transactions, Budgets
from bookeeping.core.api.serializers import BusinessSerializer, ItemsSerializer, InventorySerializer, InvoicesSerializer, PartiesSerializer, TransactionsSerializer, BudgetsSerializer

class BusinessViewSet(ModelViewSet):
    queryset = Business.objects.all()
    serializer_class = BusinessSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class ItemsViewSet(ModelViewSet):
    queryset = Items.objects.all()
    serializer_class = ItemsSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def list (self, request):
        business = request.query_params.get("business")
        if business:
            items = Items.objects.filter(business=business)
            serializer = ItemsSerializer(items, many=True)
            return Response(serializer.data)
        
        

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
    
    def list(self, request):
        business = request.query_params.get("business")
        parties = Parties.objects.filter(business=business)
        serializer = PartiesSerializer(parties, many=True)
        return Response(serializer.data)

class TransactionsViewSet(ModelViewSet):
    queryset = Transactions.objects.all()
    serializer_class = TransactionsSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def get_queryset(self):
        business = self.request.query_params.get("business")
        return Transactions.objects.filter(business=business)
        
    def perform_create(self, serializer):
        party = serializer.validated_data["party"]
        business = Business.objects.get(id=party.business.id)
        print(business)
        amount = serializer.validated_data["amount"]
        item = serializer.validated_data["item"]
        try:
            budget = Budgets.objects.get(business=business)
            budget.filter(item=item)
            if budget.remaining < amount:
                send_mail(
                    "Budget Alert",
                    f"Budget for {item} is running low",
                    ")",
                    [business.user.email],
                    fail_silently=False,
                )
        except Budgets.DoesNotExist:
            pass
        
        serializer.save()

class BudgetView(ModelViewSet):
    queryset = Budgets.objects.all()
    serializer_class = BudgetsSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    
    def list(self, request):
        business = request.query_params.get("business")
        transactions = Transactions.objects.filter(business=business)
        total_income = 0
        total_expense = 0
        for transaction in transactions:
            if transaction.transaction_type == "Income":
                total_income += transaction.amount
            else:
                total_expense += transaction.amount
        return Response(
            {
                "total_income": total_income,
                "total_expense": total_expense,
                "total_balance": total_income - total_expense,
            },
            status=status.HTTP_200_OK,
        )

class DashboardView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def get(self, request):
        business = request.query_params.get("business")
        transactions = Transactions.objects.filter(business=business)
        total_income = 0
        total_expense = 0
        for transaction in transactions:
            if transaction.transaction_type == "Income":
                total_income += transaction.amount
            else:
                total_expense += transaction.amount
        total_amount_sold = Transactions.objects.filter(type='sale').aggregate(total=Sum('amount'))['total']

        
        return Response(
            {
                "total_income": total_income,
                "total_expense": total_expense,
                "items_sold": total_amount_sold ,
                
            },
            status=status.HTTP_200_OK,
        )
        