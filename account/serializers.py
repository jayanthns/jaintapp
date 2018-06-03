from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from account.models import User
from common.custom_exception import IncorrectData


class UserSerializer(serializers.ModelSerializer):
    username = serializers.CharField(
        required=True,
        max_length=156
    )
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    password = serializers.CharField(min_length=5, write_only=True, max_length=16)
    confirm_password = serializers.CharField(min_length=5, write_only=True, max_length=16)

    def validate(self, data):
        """
        Check password and confirm password
        """
        if not data['confirm_password'] == data['password']:
            raise IncorrectData(detail="Passwords did not match. Please enter same passwords.", code=400)
        return data

    def create(self, validated_data):
        print("I AM HERE")
        user = User.objects.create_user(
            email=validated_data['email'],
            username=validated_data['username'],
            password=validated_data['password']
        )
        return user

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password', 'confirm_password')


    """
    {
        "username": "username",
        "email": "email",
        "password": "password",
        "confirm_password": "password"
    }
    """


class LoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=256, required=True)
    password = serializers.CharField(min_length=8, write_only=True, required=True)

    class Meta:
        model = User
        fields = ('email', 'password')


class UserProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'email', 'username']
