from rest_framework import viewsets

from order import models, serializers


class MerchandiseViewSet(viewsets.ModelViewSet):
    queryset = models.Merchandise.objects.all()
    serializer_class = serializers.MerchandiseSerializer


class OrderViewSet(viewsets.ModelViewSet):
    queryset = models.Order.objects.all()
    serializer_class = serializers.OrderSerializer


class BudgetViewSet(viewsets.ModelViewSet):
    queryset = models.Budget.objects.all()
    serializer_class = serializers.BudgetSerializer
