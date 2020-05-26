from django.db import models

from register.models import Address, User


class Merchandise(models.Model):
    height = models.FloatField(verbose_name='Altura')
    width = models.FloatField(verbose_name='Largura')
    weight = models.FloatField(verbose_name='Volume')
    value = models.DecimalField(decimal_places=2, max_digits=20, verbose_name='Valor')


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name='Cliente')
    origin = models.ForeignKey(Address, on_delete=models.PROTECT, related_name='order_origin', verbose_name='Origem')
    destiny = models.ForeignKey(Address, on_delete=models.PROTECT, related_name='order_destiny', verbose_name='Destino')
    date = models.DateField(verbose_name='Data')
    merchandises = models.ManyToManyField(Merchandise, verbose_name='Mercadoria')
