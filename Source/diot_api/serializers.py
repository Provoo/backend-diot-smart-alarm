from rest_framework import serializers
from django.contrib.auth.models import User

from .models import DiotDiveceTypes , DiotDivice
from rest_auth.registration.serializers import RegisterSerializer


class DiotDiveceTypesSerializer(serializers.ModelSerializer):
    class Meta:
        model = DiotDiveceTypes
        fields = '__all__'


class DiotDiviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = DiotDivice
        fields = '__all__'

class CreateUserSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

    class Meta:
        model = User
        fields = ('username', 'email', "first_name", "last_name", "id")
        read_only_fields = ('id',)
        write_only_fields = ('password',)


class MyRegisterSerializer(RegisterSerializer):
    first_name = serializers.CharField()
    last_name = serializers.CharField()

    def get_cleaned_data(self):
        super(MyRegisterSerializer, self).get_cleaned_data()
        return {
            'username': self.validated_data.get('username', ''),
            'password1': self.validated_data.get('password1', ''),
            'email': self.validated_data.get('email', ''),
            'first_name': self.validated_data.get('first_name', ''),
            'last_name': self.validated_data.get('last_name', '')
        }
