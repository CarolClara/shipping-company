from rest_framework import routers

from register import views

router = routers.SimpleRouter()
router.register(r'users', views.UserViewSet)

urlpatterns = router.urls
