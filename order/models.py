from django.db import models

from register.models import Place


class Merchandise(models.Model):
    height = models.FloatField()
    width = models.FloatField()
    weight = models.FloatField()
    value = models.DecimalField(decimal_places=2, max_digits=20)


class Order(models.Model):
    origin = Place()
    destiny = Place()
    merchandise = Merchandise()


class Budget(models.Model):
    order = Order()
    price = models.DecimalField(decimal_places=2, max_digits=20)
