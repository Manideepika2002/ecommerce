# Generated by Django 5.0.1 on 2024-03-13 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp1', '0006_formals_jeans_kurtas_tops_tshirts'),
    ]

    operations = [
        migrations.CreateModel(
            name='FormalModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/')),
                ('title', models.CharField(max_length=100)),
                ('prize', models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='formals',
        ),
        migrations.AlterField(
            model_name='jeans',
            name='image',
            field=models.ImageField(upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='kurtas',
            name='image',
            field=models.ImageField(upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='tops',
            name='image',
            field=models.ImageField(upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='tshirts',
            name='image',
            field=models.ImageField(upload_to='images/'),
        ),
    ]