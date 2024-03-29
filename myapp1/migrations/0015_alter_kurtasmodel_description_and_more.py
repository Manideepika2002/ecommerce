# Generated by Django 5.0.1 on 2024-03-14 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp1', '0014_alter_tshirtsmodel_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kurtasmodel',
            name='description',
            field=models.CharField(default=' Our kurta is beautifully detailed with sparkly sequence work that catches the eye. \nKurta Fabric is Rayon, Pant Fabric is Rayon and Dupatta Fabric is Najneen.\nPackage Contains 1 Kurta, 1 Trouser and 1 Dupatta.\nOur Sequence Work Kurta, Pant, and Dupatta Set bring you affordable elegance, making it a must-have in your ethnic wear collection.\nUpgrade your ethnic wear game with our Sequence Work Kurta, Pant, and Dupatta Set – the perfect mix of tradition, style, and budget-friendly fashion! Flaunt your style and be the star of every occasion.\n', max_length=10000),
        ),
        migrations.AlterField(
            model_name='suitsmodel',
            name='description',
            field=models.CharField(default='Get the perfect addition for your wardrobe with the Beige Knitted Jacket. This jacket boasts exceptional stretchability, keeping you warm and snug throughout the day. The slim fit design gives a cosy fit for supreme comfort. Crafted with precision, its knitted fabric ensures comfort and flexibility. Featuring full sleeves and a single-breasted front with flap pockets, this beige-hued jacket offers both style and functionality.', max_length=10000),
        ),
        migrations.AlterField(
            model_name='topsmodel',
            name='description',
            field=models.CharField(default='Rytras brings to you this beautiful Floral Printed Top which is made from Cotton fabric with beautiful print all over.This Top has been designed keeping in mind the latest trends in contemporary casual fashion. The Top combines Western with the fashion of today and makes you stand out among others when you adorn it.\n    Customers like the value, quality and appearance of the tunic. They mention that its a worthy buy, perfect to wear as formal in office as well as casually, and that its good material. They are also happy with the fit, and comfort. However, some disagree on the fabric and color.', max_length=10000),
        ),
    ]
