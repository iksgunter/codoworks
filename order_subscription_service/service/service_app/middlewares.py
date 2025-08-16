from django.http import JsonResponse
from rest_framework.authentication import TokenAuthentication
from rest_framework.exceptions import AuthenticationFailed
from subscriptions.models import UserSubscription


class ControlSubscriptionMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.token_auth = TokenAuthentication()

    def __call__(self, request):
        if request.path.startswith('/api/orders'):
            try:
                user_auth = self.token_auth.authenticate(request)
                if user_auth is not None:
                    request.user, request.auth = user_auth
            except AuthenticationFailed:
                return JsonResponse({"detail": "Требуется аутентификация."}, status=401)

            if not getattr(request, 'user', None) or not request.user.is_authenticated:
                return JsonResponse({"detail": "Требуется аутентификация."}, status=401)

            if not UserSubscription.objects.filter(user=request.user, is_active=True).exists():
                return JsonResponse({"detail": "Необходимо приобрести подписку."}, status=403)

        return self.get_response(request)