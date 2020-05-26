from django.db import models


class Address(models.Model):
    street = models.CharField(max_length=255, verbose_name='Rua')
    city = models.CharField(max_length=255, verbose_name='Cidade')
    state = models.CharField(max_length=255, verbose_name='Estado')
    country = models.CharField(max_length=255, verbose_name='País')
    zip_code = models.CharField(max_length=20, verbose_name='CEP')


class User(models.Model):
    name = models.CharField(max_length=255, verbose_name='Nome')
    email = models.EmailField(verbose_name='Email')
    cnpj = models.CharField(max_length=255, verbose_name='CNPJ')
    password = models.CharField(max_length=50, verbose_name='Senha')
    address = models.ForeignKey(Address, on_delete=models.PROTECT, verbose_name='Endereço')
