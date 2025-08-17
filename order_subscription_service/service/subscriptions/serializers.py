from django.contrib.auth import get_user_model
from rest_framework import serializers
from subscriptions.models import Tariff, UserSubscription
from service_app.config import SUBSCRIPTION_PRICES

User = get_user_model()


class TariffSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tariff
        fields = ('tariff_type', 'discount_percent')


class UserSubscriptionSerializer(serializers.ModelSerializer):
    price_with_discount = serializers.DecimalField(
        max_digits=10, decimal_places=2, read_only=True)
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.only('id'))

    class Meta:
        model = UserSubscription
        fields = ('id', 'subscribe_type', 'tariff', 'user', 'price', 'price_with_discount')
        read_only_fields = ('tariff', 'price')

    def validate(self, attrs):
        if self.instance:
            allowed_fields = {'subscribe_type'}
            extra_fields = set(self.initial_data.keys()) - allowed_fields
            if extra_fields:
                raise serializers.ValidationError(
                    f"Нельзя менять поля: {', '.join(extra_fields)}"
                )
        return attrs

    def update(self, instance, validated_data):
        subscribe_type = validated_data.get('subscribe_type')
        if subscribe_type:
            instance.subscribe_type = subscribe_type
            instance.price = SUBSCRIPTION_PRICES.get(subscribe_type, 0)
        instance.save()
        return instance
