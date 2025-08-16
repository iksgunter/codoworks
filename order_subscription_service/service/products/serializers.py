from django.contrib.auth import get_user_model
from rest_framework import serializers
from products.models import Order

User = get_user_model()


class OrderSerializer(serializers.ModelSerializer):
    total_price = serializers.DecimalField(max_digits=16, decimal_places=2, read_only=True)
    price = serializers.DecimalField(max_digits=10, decimal_places=2, read_only=True)
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.only('id'))

    class Meta:
        model = Order
        fields = ('user', 'product_name', 'price', 'quantity', 'total_price', 'created_at', 'updated_at', 'status')
        read_only_fields = ('price', 'total_price', 'created_at', 'updated_at', 'status')

    def get_total_price(self, obj):
        return obj.price * obj.quantity

    def validate(self, attrs):
        if self.instance:
            allowed_fields = {'product_name', "quantity"}
            extra_fields = set(self.initial_data.keys()) - allowed_fields
            if extra_fields:
                raise serializers.ValidationError(
                    f"Нельзя менять поля: {', '.join(extra_fields)}"
                )
        return attrs

    def create(self, validated_data):
        price = self._get_price_for_product(validated_data['product_name'])
        validated_data['price'] = price
        validated_data['status'] = 'pending'

        return Order.objects.create(**validated_data)

    def update(self, instance, validated_data):
        if 'product_name' in validated_data:
            instance.product_name = validated_data['product_name']
            instance.price = self._get_price_for_product(validated_data['product_name'])

        if 'quantity' in validated_data:
            instance.quantity = validated_data['quantity']

        instance.total_price = instance.price * instance.quantity

        instance.save()
        return instance

    def _get_price_for_product(self, product_name):
        price_map = {
            "нейро-капсула дзен-будды": 15200,
            "кибер-мандала просветления": 28400,
            "голограмма учителя пустоты": 45600,
            "дрон-лама с функцией медитации": 98700,
            "будда-бот с ИИ наставлениями": 63400,
            "арфа сознания «Ом-Цифра»": 21900,
            "капсула сна «Нейро-Сансара»": 87300,
            "имплант гармонии сердец": 50200,
            "лаборатория внутреннего света": 77800,
            "потоковый чип кармы": 14800,
            "синтезатор мантр «Будда-Флоу»": 32700,
            "голографический храм спокойствия": 92400,
            "браслет дыхания кибер-сутры": 19600,
            "каска погружения в цифровую нирвану": 86400,
            "робот-наставник по осознанности": 57200,
            "кибер-чаши поющих частот": 11800,
            "модуль тишины в дополненной реальности": 75900,
            "дрон-проводник в просветление": 68400,
            "инфо-аромат «Кибер-Сандал Плюс»": 10200,
            "сфера медитации с ИИ-потоком": 84500
        }
        return price_map.get(product_name, 0)
