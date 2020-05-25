from rest_framework import routers

from order import views

router = routers.SimpleRouter()

router.register(r'merchandises', views.MerchandiseViewSet)
router.register(r'orders', views.OrderViewSet)
router.register(r'budgets', views.BudgetViewSet)

urlpatterns = router.urls
