from hashlib import sha256

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.mixins import UpdateModelMixin, DestroyModelMixin

from Library.Serializer import IsStaff
from .Serializer import UserSerializer, CustomToken
from .models import UserModel


# Create your views here.
class RegisterView(APIView, UpdateModelMixin, DestroyModelMixin):

    @staticmethod
    def get(request):
        return Response({'msg': 'Register User'}, status=200)

    @staticmethod
    def post(request):
        create_serializer = UserSerializer(data=request.data)

        if create_serializer.is_valid():
            if UserModel.objects.filter(email=create_serializer.validated_data['email']).exists():
                return Response({"msg": "User Already Exists"}, status=403)

            create_serializer.save()
            return Response({"msg": "User registered SuccessFully"}, status=201)
        return Response({"msg": "Invalid Request"}, status=403)


class LoginView(APIView, UpdateModelMixin, DestroyModelMixin):
    @staticmethod
    def get(request):
        return Response({'msg': 'Login User'}, status=200)

    @staticmethod
    def post(request):
        serialised_user = UserSerializer(data=request.data)

        if serialised_user.is_valid():
            if UserModel.objects.filter(email=serialised_user.validated_data['email'], password=sha256(
                    serialised_user.validated_data['password'].encode()).hexdigest()).exists():
                token = CustomToken.get_token(
                    UserModel.objects.get(email=serialised_user.validated_data['email']))
                response = Response({"msg": "Logged In"}, status=status.HTTP_200_OK)

                # Set the Authorization header
                response['Authorization'] = f'Bearer {token}'
                return response

            return Response({"msg": "Wrong Credentials"}, status=200)

        return Response({"msg": "Invalid Request"}, status=403)
