# Generated by Django 5.0.1 on 2024-03-13 04:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp1', '0005_remove_customermodel_user_delete_cartmodel_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='formals',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='formals')),
                ('title', models.CharField(max_length=100)),
                ('prize', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='jeans',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='formals')),
                ('title', models.CharField(max_length=100)),
                ('prize', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='kurtas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='formals')),
                ('title', models.CharField(max_length=100)),
                ('prize', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='tops',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='formals')),
                ('title', models.CharField(max_length=100)),
                ('prize', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='tshirts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='formals')),
                ('title', models.CharField(max_length=100)),
                ('prize', models.IntegerField()),
            ],
        ),
    ]
