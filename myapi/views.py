# views.py
from django.http.response import Http404
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.serializers import Serializer
from .models import *
from .serializers import *


class CustomersViewSet(viewsets.ModelViewSet):
    queryset = Customers.objects.all().order_by('customer_id')
    serializer_class = CustomersSerializer

    def put(self, request, *args, kwargs):
        customer = Customers.objects.get()
        data = request.data
        customer.name = data["name"]
        customer.password = data["password"]
        customer.save()

        serializer = CustomersSerializer(customer)
        return Response(serializer.data)

    def delete(self, request, *args, kwargs):
        try:
            obj = Customers.objects.get()
            self.perform_destroy(obj)
        except Http404:
            pass
        return Response(status=status.HTTP_204_NO_CONTENT)


class UsersViewSet(viewsets.ModelViewSet):
    queryset = Users.objects.all().order_by('user_id')
    serializer_class = UsersSerializer

    def put(self, request, *args, kwargs):
        users = Users.objects.get()
        data = request.data
        users.name = data["name"]
        users.password = data["password"]
        users.save()

        serializer = UsersSerializer(users)
        return Response(serializer.data)

    def delete(self, request, *args, kwargs):
        try:
            obj = Users.objects.get()
            self.perform_destroy(obj)
        except Http404:
            pass
        return Response(status=status.HTTP_204_NO_CONTENT)


class OrdersViewSet(viewsets.ModelViewSet):
    queryset = Orders.objects.all().order_by('order_id')
    serializer_class = OrdersSerializer

    def put(self, request, *args, kwargs):
        orders = Orders.objects.get()
        data = request.data
        orders.customer_id = data["customer_id"]
        orders.order_date = data["order_date"]
        orders.deadline = data["deadline"]
        orders.save()

        serializer = OrdersSerializer(orders)
        return Response(serializer.data)

    def delete(self, request, *args, kwargs):
        try:
            obj = Orders.objects.get()
            self.perform_destroy(obj)
        except Http404:
            pass
        return Response(status=status.HTTP_204_NO_CONTENT)


class OrderItemsViewSet(viewsets.ModelViewSet):
    queryset = OrderItems.objects.all().order_by('order_item_id')
    serializer_class = OrderItemsSerializer

    def put(self, request, *args, kwargs):
        orderItems = OrderItems.objects.get()
        data = request.data
        orderItems.order_id = data["order_id"]
        orderItems.product_id = data["product_id"]
        orderItems.amount = data["amount"]
        orderItems.save()

        serializer = OrderItemsSerializer(orderItems)
        return Response(serializer.data)

    def delete(self, request, *args, kwargs):
        try:
            obj = OrderItems.objects.get()
            self.perform_destroy(obj)
        except Http404:
            pass
        return Response(status=status.HTTP_204_NO_CONTENT)


class ProductsViewSet(viewsets.ModelViewSet):
    queryset = Products.objects.all().order_by('product_id')
    serializer_class = ProductsSerializer

    def put(self, request, *args, kwargs):
        products = Products.objects.get()
        data = request.data
        products.product_name = data["product_name"]
        products.product_type = data["product_type"]
        products.is_salable = data["is_salable"]
        products.save()

        serializer = ProductsSerializer(products)
        return Response(serializer.data)

    def delete(self, request, *args, kwargs):
        try:
            obj = Products.objects.get()
            self.perform_destroy(obj)
        except Http404:
            pass
        return Response(status=status.HTTP_204_NO_CONTENT)


class SubProductTreeViewSet(viewsets.ModelViewSet):
    queryset = SubProductTree.objects.all().order_by('sub_product_id')
    serializer_class = SubProductTreeSerializer

    def put(self, request, *args, kwargs):
        subProductTree = SubProductTree.objects.get()
        data = request.data
        subProductTree.product_id = data["product_id"]
        subProductTree.amount = data["amount"]
        subProductTree.save()

        serializer = SubProductTreeSerializer(subProductTree)
        return Response(serializer.data)

    def delete(self, request, *args, kwargs):
        try:
            obj = SubProductTree.objects.get()
            self.perform_destroy(obj)
        except Http404:
            pass
        return Response(status=status.HTTP_204_NO_CONTENT)

    def get_queryset(self):
        p_id = self.kwargs.get("product_id")
        obj = SubProductTree.objects.filter(product_id = p_id)


class OperationsViewSet(viewsets.ModelViewSet):
    queryset = Operations.objects.all().order_by('operation_id')
    serializer_class = OperationsSerializer

    def put(self, request, *args, kwargs):
        operations = Operations.objects.get()
        data = request.data
        operations.operation_name = data["operation_name"]
        operations.product_type = data["product_type"]
        operations.save()

        serializer = OperationsSerializer(operations)
        return Response(serializer.data)

    def delete(self, request, *args, kwargs):
        try:
            obj = Operations.objects.get()
            self.perform_destroy(obj)
        except Http404:
            pass
        return Response(status=status.HTTP_204_NO_CONTENT)


class WorkCentersViewSet(viewsets.ModelViewSet):
    queryset = WorkCenters.objects.all().order_by('work_center_id')
    serializer_class = WorkCentersSerializer

    def put(self, request, *args, kwargs):
        workCenters = WorkCenters.objects.get()
        data = request.data
        workCenters.work_center_name = data["work_center_name"]
        workCenters.active = data["active"]
        workCenters.save()

        serializer = WorkCentersSerializer(workCenters)
        return Response(serializer.data)

    def delete(self, request, *args, kwargs):
        try:
            obj = WorkCenters.objects.get()
            self.perform_destroy(obj)
        except Http404:
            pass
        return Response(status=status.HTTP_204_NO_CONTENT)


class WorkCenterOperationViewSet(viewsets.ModelViewSet):
    queryset = WorkCenterOperation.objects.all().order_by('wc_opr_id')
    serializer_class = WorkCenterOperationSerializer

    def put(self, request, *args, kwargs):
        workCenterOperation = WorkCenterOperation.objects.get()
        data = request.data
        workCenterOperation.work_center_id = data["work_center_id"]
        workCenterOperation.operation_id = data["operation_id"]
        workCenterOperation.speed = data["speed"]
        workCenterOperation.save()

        serializer = WorkCenterOperationSerializer(workCenterOperation)
        return Response(serializer.data)

    def delete(self, request, *args, kwargs):
        try:
            obj = WorkCenterOperation.objects.get()
            self.perform_destroy(obj)
        except Http404:
            pass
        return Response(status=status.HTTP_204_NO_CONTENT)


class NecessaryProductsViewSet(viewsets.ModelViewSet):
    queryset = NecessaryProducts.objects.all().order_by('nc_prd_id')
    serializer_class = NecessaryProductsSerializer

    def put(self, request, *args, kwargs):
        necessaryProducts = NecessaryProducts.objects.get()
        data = request.data
        necessaryProducts.nc_prd_id = data["nc_prd_id"]
        necessaryProducts.product_name = data["product_name"]
        necessaryProducts.nc_products = data["nc_products"]
        necessaryProducts.save()

        serializer = NecessaryProductsSerializer(necessaryProducts)
        return Response(serializer.data)

    def delete(self, request, *args, kwargs):
        try:
            obj = NecessaryProducts.objects.get()
            self.perform_destroy(obj)
        except Http404:
            pass
        return Response(status=status.HTTP_204_NO_CONTENT)
