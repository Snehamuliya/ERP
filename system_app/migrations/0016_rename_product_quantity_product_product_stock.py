# Generated by Django 5.0.1 on 2024-02-10 15:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('system_app', '0015_product'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='product_quantity',
            new_name='product_stock',
        ),
    ]
