# Generated by Django 3.2.20 on 2023-08-23 23:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_products_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='Image',
            field=models.ImageField(default='blank.webp', upload_to='product_images'),
        ),
    ]
