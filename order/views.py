from copy import deepcopy
from datetime import datetime

from django.db import transaction
from rest_framework import viewsets, status
from rest_framework.response import Response

from order import models as o_models, serializers
from register import models as r_models


class PackageViewSet(viewsets.ModelViewSet):
    queryset = o_models.Package.objects.all()
    serializer_class = serializers.PackageSerializer


class OrderViewSet(viewsets.ModelViewSet):
    queryset = o_models.Order.objects.all()
    serializer_class = serializers.OrderSerializer


class DeliveryOrderViewSet(viewsets.ViewSet):

    @transaction.atomic
    def create(self, request):
        deliveries_order_json = request.data

        for delivery_order_json in deliveries_order_json:
            user = delivery_order_json.get("user")
            if not user:
                return Response(
                    data={'msg': 'Id do usuário não informado'},
                    status=status.HTTP_404_NOT_FOUND
                )

            origin = delivery_order_json.get('origin')
            destiny = delivery_order_json.get('destiny')

            try:
                origin_to_delivery = r_models.Address.objects.get(
                    zip_code=origin.get('zip_code'),
                    number=origin.get('number'),
                    street=origin.get('street'),
                    uf=origin.get('uf')
                )
            except:
                origin_to_delivery = r_models.Address.objects.create(**origin)

            try:
                destiny_to_delivery = r_models.Address.objects.get(
                    zip_code=destiny.get('zip_code'),
                    number=destiny.get('number'),
                    street=destiny.get('street'),
                    uf=destiny.get('uf')
                )
            except:
                destiny_to_delivery = r_models.Address.objects.create(**destiny)

            package = deepcopy(delivery_order_json.get('package'))
            packages_to_delivery = []

            for p in package:
                dimensions = p.get('height') + p.get('width') + p.get('length')
                products = p.pop('products')
                pkg = o_models.Package(**p, dimensions=dimensions)
                pkg.save()

                products_obj = r_models.Product.objects.filter(id__in=products)
                for products_obj in products_obj:
                    pkg.products.add(products_obj)
                pkg.save()

                packages_to_delivery.append(pkg.id)

            order_pickup_date = delivery_order_json.get('order_pickup_date')
            delivery_date = delivery_order_json.get('delivery_date')

            order = o_models.Order(
                user_id=user,
                origin=origin_to_delivery,
                destiny=destiny_to_delivery,
                order_pickup_date=datetime.strptime(order_pickup_date, '%m/%d/%Y %H:%M'),
                delivery_date=datetime.strptime(delivery_date, '%m/%d/%Y %H:%M'),
            )
            order.save()

            packages = o_models.Package.objects.filter(id__in=packages_to_delivery)
            for package in packages:
                order.packages.add(package)

            order.save()

        return Response(
            data={'msg': 'Ordem de serviço criada com sucesso'},
            status=status.HTTP_201_CREATED
        )
