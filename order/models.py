from django.db import models

from register.models import Address, User


class Merchandise(models.Model):
    height = models.FloatField()
    width = models.FloatField()
    weight = models.FloatField()
    value = models.DecimalField(decimal_places=2, max_digits=20)


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    origin = models.ForeignKey(Address, on_delete=models.PROTECT, related_name='order_origin')
    destiny = models.ForeignKey(Address, on_delete=models.PROTECT, related_name='order_destiny')
    merchandises = models.ManyToManyField(Merchandise)
