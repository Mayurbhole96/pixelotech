from rest_framework import serializers
# from .models import User
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name']
        extra_kwargs = {
            'password': {'write_only': True}
        }