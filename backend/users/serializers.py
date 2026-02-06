from rest_framework import serializers
from .models import CustomerUserModel

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = CustomerUserModel
        fields = ['id', 'first_name', 'last_name', 'username', 'email', 'role', 'password']