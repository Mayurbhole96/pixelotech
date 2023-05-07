from rest_framework import serializers
from .models import *


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = '__all__'


class UserHistorySerializer(serializers.ModelSerializer):
    # image = ImageSerializer(read_only=True)

    class Meta:
        model = UserHistory
        fields = '__all__'