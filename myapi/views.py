# views.py
from rest_framework import viewsets
from .models import *
from .serializers import *


class CustomersViewSet(viewsets.ModelViewSet):
    queryset = Customers.objects.all().order_by('customer_id')
    serializer_class = CustomersSerializer

class UsersViewSet(viewsets.ModelViewSet):
    queryset = Users.objects.all().order_by('user_id')
    serializer_class = UsersSerializer

class OrdersViewSet(viewsets.ModelViewSet):
    queryset = Orders.objects.all().order_by('order_id')
    serializer_class = OrdersSerializer

class OrderItemsViewSet(viewsets.ModelViewSet):
    queryset = OrderItems.objects.all().order_by('order_item_id')
    serializer_class = OrderItemsSerializer

class ProductsViewSet(viewsets.ModelViewSet):
    queryset = Products.objects.all().order_by('product_id')
    serializer_class = ProductsSerializer

class SubProductTreeViewSet(viewsets.ModelViewSet):
    queryset = SubProductTree.objects.all().order_by('sub_product_id')
    serializer_class = SubProductTreeSerializer

class OperationsViewSet(viewsets.ModelViewSet):
    queryset = Operations.objects.all().order_by('operation_id')
    serializer_class = OperationsSerializer

class WorkCentersViewSet(viewsets.ModelViewSet):
    queryset = WorkCenters.objects.all().order_by('work_center_id')
    serializer_class = WorkCentersSerializer

class WorkCenterOperationViewSet(viewsets.ModelViewSet):
    queryset = WorkCenterOperation.objects.all().order_by('wc_opr_id')
    serializer_class = WorkCenterOperationSerializer

