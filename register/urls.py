from rest_framework import routers

from register import views

router = routers.SimpleRouter()

router.register(r'users', views.UserViewSet)
router.register(r'address', views.AddressViewSet)

urlpatterns = router.urls
