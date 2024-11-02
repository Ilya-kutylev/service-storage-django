# Generated by Django 5.1.2 on 2024-11-02 14:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_alter_product_options_alter_product_quantity_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price_id',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='products.productprice', verbose_name='Price'),
        ),
        migrations.AlterField(
            model_name='product',
            name='quantity',
            field=models.PositiveIntegerField(verbose_name='Quantity'),
        ),
    ]
