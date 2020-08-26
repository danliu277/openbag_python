from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),
    path('admin/', admin.site.urls),
    path('customer/', include('customers.api.urls')),
    path('employee/', include('employees.api.urls')),
    path('game/', include('games.api.urls')),
    path('purchaseOrder/', include('purchase_orders.api.urls')),
    path('sale/', include('sales.api.urls')),
    path('vendor/', include('vendors.api.urls')),
]