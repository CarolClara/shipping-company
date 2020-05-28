from rest_framework import viewsets

from order import models, serializers


class MerchandiseViewSet(viewsets.ModelViewSet):
    queryset = models.Package.objects.all()
    serializer_class = serializers.MerchandiseSerializer


class OrderViewSet(viewsets.ModelViewSet):
    queryset = models.Order.objects.all()
    serializer_class = serializers.OrderSerializer


class CreateOrderViewSet(viewsets.ViewSet):

    def create(self, request):
        pass
