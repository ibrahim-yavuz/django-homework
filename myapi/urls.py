# myapi/urls.py
from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'customers', views.CustomersViewSet)
router.register(r'users', views.UsersViewSet)
router.register(r'orders', views.OrdersViewSet)
router.register(r'orderitems', views.OrderItemsViewSet)
router.register(r'products', views.ProductsViewSet)
router.register(r'subproducttree', views.SubProductTreeViewSet)
router.register(r'operations', views.OperationsViewSet)
router.register(r'workcenters', views.WorkCentersViewSet)
router.register(r'workcenteroperation', views.WorkCenterOperationViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]