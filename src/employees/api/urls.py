from employees.api.views import EmployeeViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'', EmployeeViewSet, basename='employee')
urlpatterns = router.urls