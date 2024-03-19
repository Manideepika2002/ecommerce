# Generated by Django 5.0.1 on 2024-03-14 07:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp1', '0012_alter_formalmodel_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='formalmodel',
            name='description',
            field=models.CharField(default='Unwrap the essence of luxury with the Black Temp Tech Check Shirt. Designed for the modern man, this shirt boasts 37.5°C temperature regulation technology, ensuring optimal comfort all day. It has odour protection that adds an extra layer of confidence. The sleek black hue and classic check pattern make a bold statement, while the semi-cutaway collar and India slim fit add a touch of contemporary flair. Crafted with woven fabric, it features full sleeves, a button closure, and a chest pocket for added convenience.', max_length=10000),
        ),
        migrations.AlterField(
            model_name='tshirtsmodel',
            name='description',
            field=models.CharField(default='Make a stylish statement with your looks by donning this Black Polo Neck T-Shirt. The classic polo neck and half sleeves offer a timeless and appealing look, while the slim-fitting silhouette enhances and complements your natural body shape. Crafted in meticulously knitted, this t-shirt is a wardrobe essential embodiment of casual style. The stunning black colour gives your t-shirt a ravishing touch to uplift your overall attire.\n\n● Stretchable fabric delivers unparalleled comfort.\n● Pair this t-shirt with Blackberrys trousers, a blazer and leather sneakers for a sharp, casual, refined look.\n\nFabric Composition\n95% Cotton 5% Spandex', max_length=10000),
        ),
    ]