# Generated by Django 4.2.13 on 2024-07-12 05:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Business',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('address', models.TextField(blank=True)),
                ('phone', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('website', models.URLField(blank=True)),
                ('description', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Parties',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('customer', 'Customer'), ('supplier', 'Supplier'), ('employee', 'Employee'), ('other', 'Other')], max_length=20)),
                ('name', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=20)),
                ('balance', models.DecimalField(decimal_places=2, max_digits=10)),
                ('business', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.business')),
            ],
        ),
        migrations.CreateModel(
            name='Transactions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('purchase', 'Purchase'), ('sale', 'Sale'), ('expense', 'Expense'), ('income', 'Income'), ('payment', 'Payment'), ('receipt', 'Receipt'), ('transfer', 'Transfer')], max_length=20)),
                ('date', models.DateField()),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('description', models.TextField(blank=True)),
                ('party', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.parties')),
            ],
        ),
        migrations.CreateModel(
            name='Items',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True)),
                ('cost_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('selling_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('quantity', models.PositiveIntegerField()),
                ('business', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.business')),
            ],
        ),
        migrations.CreateModel(
            name='Invoices',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('purchase', 'Purchase'), ('sale', 'Sale'), ('expense', 'Expense'), ('income', 'Income')], max_length=20)),
                ('date', models.DateField()),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('description', models.TextField(blank=True)),
                ('party', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.parties')),
            ],
        ),
        migrations.CreateModel(
            name='Inventory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField()),
                ('date', models.DateField()),
                ('business', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.business')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.items')),
            ],
        ),
        migrations.CreateModel(
            name='Budgets',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('business', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.business')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.items')),
            ],
        ),
    ]
