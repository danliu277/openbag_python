from purchase_orders.api.views import PurchaseOrderViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'', PurchaseOrderViewSet, basename='purchaseOrder')
urlpatterns = router.urls