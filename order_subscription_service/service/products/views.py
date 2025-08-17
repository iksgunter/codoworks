import logging
import requests
from django.conf import settings
from django.db.models import ExpressionWrapper, F, DecimalField
from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from products.models import Order
from products.serializers import OrderSerializer
from subscriptions.permissions import HasActiveSubscription

logger = logging.getLogger(__name__)


class OrderView(ModelViewSet):
    queryset = Order.objects.annotate(
        total_price=ExpressionWrapper(F("price") * F("quantity"),
        output_field=DecimalField(max_digits=10, decimal_places=2))).all()
    serializer_class = OrderSerializer
    lookup_field = "pk"
    permission_classes = [HasActiveSubscription]

    def perform_create(self, serializer):
        instance = serializer.save()
        try:
            logger.info(f"Отправляю заказ {instance.id} в Telegram...")
            response = requests.post(
                f"https://api.telegram.org/bot{settings.TELEGRAM_BOT_TOKEN}/sendMessage",
                json={
                    "chat_id": instance.user.telegram_id,
                    "text": f"Вам пришёл новый заказ! #{instance.id}"
                }
            )
            logger.info(f"Ответ Telegram API: {response.status_code} {response.text}")
        except Exception as e:
            logger.error(f"Ошибка при отправке уведомления: {e}")
