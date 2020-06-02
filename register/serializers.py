from rest_framework import serializers

from register import models


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Address
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = '__all__'

    def to_representation(self, instance):
        self.fields['address'] = AddressSerializer(read_only=True)
        return super(UserSerializer, self).to_representation(instance)


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Product
        fields = '__all__'
