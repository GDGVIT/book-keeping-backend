# Generated by Django 4.2.13 on 2024-07-17 11:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_business_user_alter_business_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='transactions',
            name='item',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='core.items'),
            preserve_default=False,
        ),
    ]
