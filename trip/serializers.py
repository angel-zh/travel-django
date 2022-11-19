from rest_framework import serializers
from .models.hotel import Hotel
from .models.flight import Flight
from .models.traveller import Traveller
from .models.booking import Booking


class HotelSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Hotel

class FlightSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Flight

class TravellerSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Traveller

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Booking

class BookingReadSerializer(serializers.ModelSerializer):
    traveller = serializers.StringRelatedField()
    flight = serializers.StringRelatedField()
    hotel = serializers.StringRelatedField()
    class Meta:
        fields = '__all__'
        model = Booking
