from django.db import models
import jsonfield

class Customers(models.Model):
    customer_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=60)
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Users(models.Model):
    user_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=60)
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Orders(models.Model):
    order_id = models.AutoField(primary_key=True)
    customer_id = models.PositiveIntegerField()
    order_date = models.DateField()
    deadline = models.DateField()

    def __str__(self):
        return str(self.order_id)

class Products(models.Model):
    product_id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=60)
    product_type = models.CharField(max_length=50)
    is_salable = models.BooleanField()

    def __str__(self):
        return self.product_name


class SubProductTree(models.Model):
    sub_product_id = models.AutoField(primary_key=True)
    product_id = models.PositiveIntegerField()
    amount = models.PositiveIntegerField()

    def __str__(self):
        return str(self.sub_product_id)

class Operations(models.Model):
    operation_id = models.AutoField(primary_key=True)
    operation_name = models.CharField(max_length=60)
    product_type = models.CharField(max_length=50)

    def __str__(self):
        return self.operation_name

class WorkCenters(models.Model):
    work_center_id = models.AutoField(primary_key=True)
    work_center_name = models.CharField(max_length=60)
    active = models.BooleanField()

    def __str__(self):
        return self.work_center_name

class WorkCenterOperation(models.Model):
    wc_opr_id = models.AutoField(primary_key=True)
    work_center_id = models.PositiveIntegerField()
    operation_id = models.PositiveIntegerField()
    speed = models.PositiveIntegerField()

    def __str__(self):
        return str(self.wc_opr_id)

class OrderItems(models.Model):
    order_item_id = models.AutoField(primary_key=True)
    order_id = models.PositiveIntegerField()
    product_id = models.PositiveIntegerField()
    amount = models.PositiveIntegerField()

    def __str__(self):
        return str(self.order_item_id)

class NecessaryProducts(models.Model):
    nc_prd_id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=40)
    nc_products = jsonfield.JSONField(max_length=40)

    def __str__(self):
        return str(self.product_name)
