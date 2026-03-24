from rest_framework.routers import DefaultRouter
from resources.views import ResourceViewSet
from locations.views import LocationViewSet
from reviews.views import ReviewViewSet

router = DefaultRouter()
router.register(r'resources', ResourceViewSet)
router.register(r'locations', LocationViewSet)
router.register(r'reviews', ReviewViewSet)

urlpatterns = router.urls