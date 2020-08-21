from sales.api.views import SalesViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'', SalesViewSet, basename='sale')
urlpatterns = router.urls