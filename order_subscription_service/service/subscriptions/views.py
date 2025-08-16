from django.db.models import ExpressionWrapper, F, DecimalField
from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from subscriptions.models import UserSubscription, Tariff
from subscriptions.serializers import TariffSerializer, UserSubscriptionSerializer


class TariffView(ReadOnlyModelViewSet):
    queryset = Tariff.objects.only('tariff_type', 'discount_percent')
    serializer_class = TariffSerializer


class UserSubscriptionView(ModelViewSet):
    queryset = (
        UserSubscription.objects
        .select_related("tariff", "user")
        .annotate(
            price_with_discount=ExpressionWrapper(
                F("price") * (100 - F("tariff__discount_percent")) / 100.0,
                output_field=DecimalField(max_digits=10, decimal_places=2)
            )
        )
        .only("id", "subscribe_type", "price", "tariff__tariff_type", "tariff__discount_percent", "user__id",  "user")
    )
    serializer_class = UserSubscriptionSerializer
    lookup_field = "pk"



