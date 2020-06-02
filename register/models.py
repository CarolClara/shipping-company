from django.db import models


class Address(models.Model):
    street = models.CharField(max_length=255, verbose_name='Rua')
    complement = models.CharField(max_length=255, verbose_name='Complemento')
    neighborhood = models.CharField(max_length=255, verbose_name='Bairro')
    locality = models.CharField(max_length=255, verbose_name='Localidade')
    uf = models.CharField(max_length=255, verbose_name='UF')
    number = models.CharField(max_length=10, verbose_name='Número')
    zip_code = models.CharField(max_length=20, verbose_name='CEP')


class User(models.Model):
    name = models.CharField(max_length=255, verbose_name='Nome')
    email = models.EmailField(verbose_name='Email')
    cnpj = models.CharField(max_length=255, verbose_name='CNPJ')
    password = models.CharField(max_length=50, verbose_name='Senha')
    address = models.ForeignKey(Address, on_delete=models.PROTECT, verbose_name='Endereço')


class Product(models.Model):
    name = models.CharField(max_length=255, verbose_name='Nome do produto')
    description = models.CharField(max_length=255, blank=True, null=True, verbose_name='Descrição')
