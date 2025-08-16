from django.db.models import ExpressionWrapper, F, DecimalField
from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from products.models import Order
from products.serializers import OrderSerializer
from subscriptions.permissions import HasActiveSubscription


class OrderView(ModelViewSet):
    queryset = Order.objects.annotate(
        total_price=ExpressionWrapper(F("price") * F("quantity"),
        output_field=DecimalField(max_digits=10, decimal_places=2))).all()
    serializer_class = OrderSerializer
    lookup_field = "pk"
    permission_classes = [HasActiveSubscription]
