import logging
import requests
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver

from products.models import Order

logger = logging.getLogger(__name__)


@receiver(post_save, sender=Order)
def notify_telegram(sender, instance, created, **kwargs):
    if created:
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
