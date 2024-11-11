from rest_framework import serializers

from bookeeping.core.models import Business, Items, Inventory, Invoices, Parties, Transactions, Budgets

class BusinessSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = Business
        fields = '__all__'

class ItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Items
        fields = '__all__'

class InventorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Inventory
        fields = '__all__'

class InvoicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Invoices
        fields = '__all__'

class PartiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parties
        fields = '__all__'

class TransactionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transactions
        fields = '__all__'

class BudgetsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Budgets
        fields = '__all__'

