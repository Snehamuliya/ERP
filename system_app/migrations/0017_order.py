# Generated by Django 5.0.1 on 2024-02-11 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('system_app', '0016_rename_product_quantity_product_product_stock'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_name', models.CharField(max_length=60)),
                ('customer_address', models.CharField(max_length=90)),
                ('customer_mobile', models.CharField(max_length=14)),
                ('product_name', models.CharField(max_length=30)),
                ('product_price', models.CharField(max_length=9)),
                ('product_Qty', models.CharField(max_length=4)),
                ('total', models.CharField(max_length=60)),
                ('date', models.CharField(max_length=15)),
            ],
            options={
                'db_table': 'order',
            },
        ),
    ]
