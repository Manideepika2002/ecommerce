# Generated by Django 5.0.1 on 2024-03-18 13:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp1', '0027_alter_profilemodel_password'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profilemodel',
            name='user',
        ),
    ]
