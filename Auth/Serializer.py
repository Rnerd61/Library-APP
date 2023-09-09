from rest_framework import serializers
from hashlib import sha256
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.tokens import Token
from .models import UserModel


class UserSerializer(serializers.ModelSerializer):
    email = serializers.CharField(max_length=50, required=True)
    password = serializers.CharField(max_length=50, required=True)
    role = serializers.CharField(max_length=50)

    def create(self, validated_data):
        email = validated_data.get('email')
        password = sha256(validated_data.get('password').encode()).hexdigest()
        role = validated_data['role']

        return UserModel.objects.create(
            email=email,
            password=password,
            role=role
        )

    class Meta:
        model = UserModel
        fields = (
            'email',
            'password',
            'role',
        )


class ForgotSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=50, required=True)
    password = serializers.CharField(max_length=50, required=True)
    new_password = serializers.CharField(max_length=50, required=True)

    def update(self, instance, validated_data):
        instance.email = validated_data.get('email', instance.email)
        instance.password = sha256(validated_data.get('password', instance.password).encode()).hexdigest()
        exists = 0

        try:
            user = UserModel.objects.get(email=instance.email, password=instance.password)
            exists = 1
        except:
            pass

        if exists:
            user.set_password(sha256(validated_data.get('new_password')).hexdigest())
            user.save()

            return "password Updated Successfully"

    class Meta:
        model = UserModel
        fields = (
            'email',
            'password',
            'new_password',
        )


class CustomeToken(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user):
        token = super(CustomeToken, cls).get_token(user)
        token['token_type'] = 'access'
        token['username'] = user.email
        token['role'] = user.role
        return token