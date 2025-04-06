import jwt  # type: ignore
from jwt.exceptions import ExpiredSignatureError, InvalidTokenError  # type: ignore
from rest_framework.authentication import BaseAuthentication  # type: ignore
from rest_framework.exceptions import AuthenticationFailed  # type: ignore
from django.conf import settings
from django.contrib.auth import get_user_model
from datetime import datetime, timedelta


class TokenAuthentication(BaseAuthentication):
    def authenticate(self, request):
        token = self.extract_token(request)
        if token is None:
            return None

        try:
            payload = jwt.decode(token, key=settings.SECRET_KEY, algorithms=["HS256"])
            self.verify_token(payload)
            user_id = payload.get("id")
            user = get_user_model().objects.get(id=user_id)
            return (user, token)
        except (
            InvalidTokenError,
            ExpiredSignatureError,
            get_user_model().DoesNotExist,
        ):
            raise AuthenticationFailed("Invalid or expired token")

    def verify_token(self, payload):
        if "exp" not in payload:
            raise AuthenticationFailed("Token is missing expiration time")

        expiration = payload["exp"]
        current_time = datetime.now().timestamp()
        if current_time > expiration:
            raise AuthenticationFailed("Token has expired")

    def extract_token(self, request):
        auth_header = request.headers.get("Authorization", None)
        if not auth_header:
            return None

        parts = auth_header.split(" ")
        if len(parts) != 2 or parts[0] != "Bearer":
            raise AuthenticationFailed("Invalid authentication header")

        token = parts[1]
        if not token:
            raise AuthenticationFailed("Token is missing")

        return token

    @staticmethod
    def generate_token(payload):
        expiration = datetime.now() + timedelta(hours=24)
        payload["exp"] = int(expiration.timestamp())
        token = jwt.encode(payload=payload, key=settings.SECRET_KEY, algorithm="HS256")
        return token
