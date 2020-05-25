from django.shortcuts import render
from rest_framework import viewsets

from register import serializers
from register.models import User


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer
