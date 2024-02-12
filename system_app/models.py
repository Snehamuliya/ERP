from django.db import models

# Create your models here.
class Feedback(models.Model):
    fullname = models.CharField(max_length=60)
    email = models.CharField(max_length=40)
    feedback = models.TextField()
    class Meta:
        db_table = "feedback"

    # class Meta used to rename system_app_feedback to only feedback


class Supplier(models.Model):
    supplier_name = models.CharField(max_length=60)
    supplier_address = models.CharField(max_length=90)
    supplier_contact = models.CharField(max_length=14)
    supplier_mail = models.CharField(max_length=60)
    supplier_comp_name = models.CharField(max_length=60)
    supplier_comp_address = models.CharField(max_length=90)
    supplier_comp_mail = models.CharField(max_length=60)    
    supplier_comp_bank = models.CharField(max_length=40)
    supplier_comp_acc = models.CharField(max_length=20) 
    supplier_user = models.CharField(max_length=40)
    supplier_password = models.CharField(max_length=60)    
    class Meta:
        db_table = "supplier"

    # class Meta used to rename system_app_supplier to only supplier
        


class Customer(models.Model):
    customer_name = models.CharField(max_length=60)
    customer_address = models.CharField(max_length=90)
    customer_contact = models.CharField(max_length=14)
    customer_mail = models.CharField(max_length=60)
    customer_user = models.CharField(max_length=40)
    customer_password= models.CharField(max_length=60)    
    class Meta:
        db_table = "customer"


class Product(models.Model):
    product_name = models.CharField(max_length=60)
    product_price = models.CharField(max_length=90)
    product_category = models.CharField(max_length=14)
    product_unit = models.CharField(max_length=60)
    product_stock = models.CharField(max_length=40)   
    class Meta:
        db_table = "product"


class Order(models.Model):
    user_name = models.CharField(max_length=60)    
    customer_name = models.CharField(max_length=60)
    customer_address = models.CharField(max_length=90)
    customer_mobile = models.CharField(max_length=14)
    product_id = models.CharField(max_length=30)    
    product_name = models.CharField(max_length=30)
    product_price = models.CharField(max_length=9)
    product_Qty = models.CharField(max_length=4)
    order_total = models.CharField(max_length=5)
    order_date = models.CharField(max_length=15) 
    class Meta:
        db_table = "order"


class Stock(models.Model):
    product_id = models.CharField(max_length=5)    
    product_name = models.CharField(max_length=30)
    product_price = models.CharField(max_length=9)
    product_unit = models.CharField(max_length=4)
    add_stock = models.CharField(max_length=5)
    Stock_date = models.CharField(max_length=15) 
    class Meta:
        db_table = "stock"