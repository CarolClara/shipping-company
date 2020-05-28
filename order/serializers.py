from rest_framework import serializers

from order import models
from register.serializers import AddressSerializer


class MerchandiseSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Package
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Order
        fields = '__all__'

    def to_representation(self, instance):
        self.fields['merchandises'] = MerchandiseSerializer(many=True)
        self.fields['origin'] = AddressSerializer()
        self.fields['destiny'] = AddressSerializer()
        return super(OrderSerializer, self).to_representation(instance)
