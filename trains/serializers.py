from rest_framework import serializers
from .models import Train

class TrainSearchSerializer(serializers.Serializer):
    source = serializers.CharField()
    destination = serializers.CharField()

class TrainListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Train
        fields = '__all__'

