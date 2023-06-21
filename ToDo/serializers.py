from rest_framework import serializers
from rest_framework_simplejwt.serializers import (
    TokenRefreshSerializer, TokenObtainPairSerializer
)
from rest_framework_simplejwt.exceptions import AuthenticationFailed
from rest_framework_simplejwt.tokens import RefreshToken, AccessToken

from django.core.exceptions import ObjectDoesNotExist

from .models import Affairs, User

class TokenObtainPairSerializer(TokenObtainPairSerializer):

    def validate(self, *args, **kwargs):
        data = super().validate(*args, **kwargs)

        if not self.user.is_active:
            raise AuthenticationFailed({
                'detail': f"Пользователь {self.user.login} был деактивирован!"
            }, code='user_deleted')

        data['id'] = self.user.id
        data['login'] = self.user.login

        return data

class TokenRefreshSerializer(TokenRefreshSerializer):
    
    def validate(self, attrs):
        data = super().validate(attrs)
        refresh = RefreshToken(attrs['refresh'])

        try:
            user = User.objects.get(
                pk=refresh.payload.get('user_id')
            )
        except ObjectDoesNotExist:
            raise serializers.ValidationError({
                'detail': f"Пользователь был удалён!"
            }, code='user_does_not_exists')

        if user.blocked:
            raise AuthenticationFailed({
                'detail': f"Пользователь {user.login} был заблокирован!"
            }, code='user_deleted')

        data['id'] = user.id
        data['login'] = user.login

        return data


class GetUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class RegisterUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['login', 'password', 'email']

# Affair
class AffairsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Affairs
        fields = '__all__'