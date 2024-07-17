from django.db import models

class Business(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField(blank=True)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    website = models.URLField(blank=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name
    
class Parties(models.Model):
    type_choices = (
        ('customer', 'Customer'),
        ('supplier', 'Supplier'),
        ('employee', 'Employee'),
        ('other', 'Other')
    )
    type = models.CharField(max_length=20, choices=type_choices)
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    balance = models.DecimalField(max_digits=10, decimal_places=2)
    business = models.ForeignKey(Business, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Transactions(models.Model):
    type_choices = (
        ('purchase', 'Purchase'),
        ('sale', 'Sale'),
        ('expense', 'Expense'),
        ('income', 'Income'),
        ('payment', 'Payment'),
        ('receipt', 'Receipt'),
        ('transfer', 'Transfer')
    )
    type = models.CharField(max_length=20, choices=type_choices)
    date = models.DateField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True)
    party = models.ForeignKey(Parties, on_delete=models.CASCADE)

    def __str__(self):
        return self.type

class Items(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    cost_price = models.DecimalField(max_digits=10, decimal_places=2)
    selling_price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField()
    business = models.ForeignKey(Business, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Inventory(models.Model):
    item = models.ForeignKey(Items, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    date = models.DateField()
    business = models.ForeignKey(Business, on_delete=models.CASCADE)

    def __str__(self):
        return self.item.name

class Invoices(models.Model):
    type_choices = (
        ('purchase', 'Purchase'),
        ('sale', 'Sale'),
        ('expense', 'Expense'),
        ('income', 'Income')
    )
    type = models.CharField(max_length=20, choices=type_choices)
    date = models.DateField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True)
    party = models.ForeignKey(Parties, on_delete=models.CASCADE)

    def __str__(self):
        return self.type

class Budgets(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    item= models.ForeignKey(Items, on_delete=models.CASCADE)
    business = models.ForeignKey(Business, on_delete=models.CASCADE)

    @property
    def remaining(self):
        transactions = Transactions.objects.filter(item=self.item)
        total = 0
        for transaction in transactions:
            if transaction.type == "Purchase":
                total += transaction.amount
            else:
                total -= transaction.amount
        return self.amount - total

    def __str__(self):
        return self.type