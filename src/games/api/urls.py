from games.api.views import GameViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'', GameViewSet, basename='game')
urlpatterns = router.urls