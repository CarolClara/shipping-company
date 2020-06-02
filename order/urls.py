from rest_framework import routers

from order import views

router = routers.SimpleRouter()

router.register(r'packages', views.PackageViewSet)
router.register(r'orders', views.OrderViewSet)
router.register(r'create_delivery_order', views.DeliveryOrderViewSet, basename='delivery_order')

urlpatterns = router.urls
