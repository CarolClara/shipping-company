from django.db import models


class Place(models.Model):
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    zip_code = models.CharField(max_length=20)


class User(models.Model):

    name = models.CharField(max_length=255)
    email = models.EmailField()
    cnpj = models.CharField(max_length=255)
    password = models.CharField(max_length=50)
    address = Place()
