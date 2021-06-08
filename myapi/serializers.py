# serializers.py
from rest_framework import serializers
from .models import *

class WorkCenterOperationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = WorkCenterOperation
        fields = ('wc_opr_id', 'work_center_id', 'operation_id', 'speed')

class WorkCentersSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = WorkCenters
        fields = ('work_center_id', 'work_center_name', 'active')

class OperationsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Operations
        fields = ('operation_id', 'operation_name', 'product_type')

class SubProductTreeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SubProductTree
        fields = ('sub_product_id', 'product_id', 'amount')
class ProductsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Products
        fields = ('product_id', 'product_name', 'product_type','is_salable')

class CustomersSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Customers
        fields = ('customer_id', 'name' , 'password')

class UsersSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Users
        fields = ('user_id', 'name' , 'password')

class OrdersSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Orders
        fields = ('order_id', 'customer_id' , 'order_date' , 'deadline')

class OrderItemsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = OrderItems
        fields = ('order_item_id', 'order_id' , 'product_id', 'amount')

class NecessaryProductsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = NecessaryProducts
        fields = ('nc_prd_id', 'product_name' , 'nc_products')