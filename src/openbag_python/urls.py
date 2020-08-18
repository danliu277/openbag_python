from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),
    path('admin/', admin.site.urls),
    path('customer/', include('customers.api.urls')),
    path('employee/', include('employees.api.urls')),
]