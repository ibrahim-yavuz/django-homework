from django.contrib import admin
from .models import *

admin.site.register(Customers)
admin.site.register(Users)
admin.site.register(Orders)
admin.site.register(Products)
admin.site.register(SubProductTree)
admin.site.register(Operations)
admin.site.register(WorkCenters)
admin.site.register(WorkCenterOperation)
admin.site.register(OrderItems)
admin.site.register(NecessaryProducts)
