# Generated by Django 5.0.1 on 2024-03-18 18:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp1', '0034_remove_cartitem_cart_remove_cartitem_price_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartitem',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='myapp1.formalmodel'),
        ),
    ]
