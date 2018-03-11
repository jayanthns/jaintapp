from django.contrib.auth import authenticate
from django.http import HttpResponse
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from account.models import User
from account.serializers import UserSerializer, LoginSerializer, UserProfileSerializer
from common.custom_exception import AuthFailed, IncorrectData


@api_view(['GET'])
def index(request):
    return Response("HELLO WORLD", status=status.HTTP_200_OK)


class RegisterUser(APIView):
    """
    Creates the User
    """

    permission_classes = (AllowAny, )

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            if user:
                return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginUser(APIView):
    """
    Login User
    """

    permission_classes = (AllowAny,)

    def post(self, request):
        print("I AM HERE")
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = authenticate(
                email=request.data['email'].lower(),
                password=request.data['password']
            )
            if not user:
                raise AuthFailed(detail=None, code=None)

            token = Token.objects.get_or_create(user=user)
            print(token)
            return Response({"token": token[0].key, "email": user.email, "username": user.username}, status=status.HTTP_200_OK)

        raise IncorrectData(detail=serializer.errors, code=None)


class UserProfileAPI(APIView):
    authentication_classes = [TokenAuthentication, ]
    permission_classes = (IsAuthenticated, )

    def get(self, request):
        print(request.auth.user)
        serializer = UserProfileSerializer(request.auth.user).data
        return Response(serializer, status=status.HTTP_200_OK)