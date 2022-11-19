from django.shortcuts import render, get_object_or_404
from ..serializers import HotelSerializer
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from ..models.hotel import Hotel


# Create your views here.

# localhost:8000/trip/hotels/ ---> get, post

class HotelsView(APIView):
    """View class for hotels/ for viewing all and creating a hotel trip"""
    serializer_class = HotelSerializer
    def get(self, request):
        hotels = Hotel.objects.all()
        serializer = HotelSerializer(hotels, many=True)
        return Response({'hotels': serializer.data})

    def post(self, request):
        serializer = HotelSerializer(data=request.data)
        # serializer is used as a validation tool and will check to see if incoming data satisfies the fields in our model
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# localhost:8000/trip/hotels/:id ---> get, patch, delete

class HotelDetailView(APIView):
    """View class for hotels/:pk for viewing, updating, and removing a single hotel trip"""
    serializer_class = HotelSerializer
    def get(self, request, pk):
        hotel = get_object_or_404(Hotel, pk=pk)
        serializer = HotelSerializer(hotel)
        return Response({'hotel': serializer.data})

    def patch(self, request, pk):
        hotel = get_object_or_404(Hotel, pk=pk)
        serializer = HotelSerializer(hotel, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        hotel = get_object_or_404(Hotel, pk=pk)
        hotel.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
