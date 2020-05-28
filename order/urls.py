from rest_framework import routers

from order import views

router = routers.SimpleRouter()

router.register(r'merchandises', views.MerchandiseViewSet)
router.register(r'orders', views.OrderViewSet)

urlpatterns = router.urls
