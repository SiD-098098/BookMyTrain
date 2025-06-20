from rest_framework import serializers
from .models import Booking
from trains.serializers import TrainListSerializer

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'
        read_only_fields = ['user', 'seat_number']


class BookingResponseSerializer(serializers.ModelSerializer):
    train = TrainListSerializer(read_only = True)
    class Meta:
        model = Booking
        fields = '__all__'
        read_only_fields = ['user', 'seat_number']

        