from sales.api.views import SaleViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'', SaleViewSet, basename='sale')
urlpatterns = router.urls