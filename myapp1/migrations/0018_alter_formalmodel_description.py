# Generated by Django 5.0.1 on 2024-03-14 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp1', '0017_tshirtsmodel_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='formalmodel',
            name='description',
            field=models.CharField(max_length=10000),
        ),
    ]