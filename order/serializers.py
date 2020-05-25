from rest_framework import serializers

from order import models


class MerchandiseSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Merchandise
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Order
        fields = '__all__'


class BudgetSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Budget
        fields = '__all__'
