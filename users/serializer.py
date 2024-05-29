from rest_framework import serializers
from .models import Coach, Client, User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class CoachSerializer(serializers.ModelSerializer):

    class Meta:
        model = Coach
        fields = '__all__'


class ClientSerializer(serializers.ModelSerializer):

    class Meta:
        model = Client
        fields = '__all__'
