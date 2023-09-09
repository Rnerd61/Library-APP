from rest_framework import serializers
from hashlib import sha256
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.tokens import Token
from .models import UserModel


class UserSerializer(serializers.ModelSerializer):
    email = serializers.CharField(max_length=50, required=True)
    password = serializers.CharField(max_length=50, required=True)

    def create(self, validated_data):
        email = validated_data.get('email')
        password = sha256(validated_data.get('password').encode()).hexdigest()

        return UserModel.objects.create(
            email=email,
            password=password
        )

    class Meta:
        model = UserModel
        fields = (
            'email',
            'password',
        )


class CustomToken(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user):
        token = super(CustomToken, cls).get_token(user)
        token['token_type'] = 'access'
        token['email'] = user.email
        token['is_staff'] = user.is_staff
        return token
