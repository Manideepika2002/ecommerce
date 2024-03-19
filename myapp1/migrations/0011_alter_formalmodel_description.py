# Generated by Django 5.0.1 on 2024-03-14 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp1', '0010_formalmodel_description_kurtasmodel_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='formalmodel',
            name='description',
            field=models.CharField(default='Unwrap the essence of luxury with the Black Temp Tech Check Shirt. Designed for the modern man, this shirt boasts 37 temperature regulation technology, ensuring optimal comfort all day. It has odour protection that adds an extra layer of confidence. The sleek black hue and classic check pattern make a bold statement, while the semi-cutaway collar and India slim fit add a touch of contemporary flair. Crafted with woven fabric, it features full sleeves, a button closure, and a chest pocket for added convenience.', max_length=10000),
        ),
    ]