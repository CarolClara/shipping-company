from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', include('register.urls')),
    path('orders/', include('order.urls'))
]
