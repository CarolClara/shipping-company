from datetime import datetime

from django.db import models

from register import models as register_models


class Package(models.Model):
    products = models.ManyToManyField(register_models.Product, verbose_name='Produtos')
    height = models.FloatField(verbose_name='Altura do pacote (cm)')
    width = models.FloatField(verbose_name='Largura do pacote (cm)')
    length = models.FloatField(verbose_name='Comprimento do pacote (cm)')
    dimensions = models.FloatField(verbose_name='Dimensões (cm)')
    weight = models.FloatField(verbose_name='Peso do pacote (kg)')
    quantity_of_packages = models.IntegerField(verbose_name='Quantidade de pacotes')
    value = models.DecimalField(decimal_places=2, max_digits=20, verbose_name='Valor total do pacote')


class Order(models.Model):
    user = models.ForeignKey(register_models.User, on_delete=models.PROTECT, verbose_name='Cliente')
    origin = models.ForeignKey(
        register_models.Address, on_delete=models.PROTECT, related_name='order_origin', verbose_name='Origem'
    )
    destiny = models.ForeignKey(
        register_models.Address, on_delete=models.PROTECT, related_name='order_destiny', verbose_name='Destino'
    )
    creation_date = models.DateTimeField(verbose_name='Data e hora da criação', default=datetime.now())
    order_pickup_date = models.DateTimeField(verbose_name='Data e hora da retirada')
    delivery_date = models.DateTimeField(verbose_name='Data e hora da entrega')
    packages = models.ManyToManyField(Package, verbose_name='Pacotes')
