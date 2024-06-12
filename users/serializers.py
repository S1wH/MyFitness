from rest_framework import serializers
from .models import Coach, Client, User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password', 'is_superuser', 'first_name', 'last_name', 'email', 'is_verified']
        read_only_fields = ['is_superuser', 'is_verified']


class CoachSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Coach
        fields = '__all__'


class ClientSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Client
        fields = '__all__'
