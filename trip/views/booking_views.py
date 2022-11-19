from django.shortcuts import render, get_object_or_404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from ..models.booking import Booking
from ..serializers import BookingSerializer, BookingReadSerializer

# Create your views here.
#localhost:8000/trip/bookings/ get post
class BookingsView(APIView):
    """View class for bookings/ for viewing all and creating"""
    serializer_class = BookingSerializer
    def get(self, request):
        bookings = Booking.objects.all()
        serializer = BookingReadSerializer(bookings, many=True)
        return Response({'bookings': serializer.data})

    def post(self, request):
        serializer = BookingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#localhost:8000/trip/bookings/:id get delete update
class BookingDetailView(APIView):
    """View class for bookings/:pk for viewing a single booking, updating a single booking, or removing a single booking"""
    serializer_class = BookingSerializer
    def get(self, request, pk):
        booking = get_object_or_404(Booking, pk=pk)
        serializer = BookingReadSerializer(booking)
        return Response({'booking': serializer.data})

    def patch(self, request, pk):
        booking = get_object_or_404(Booking, pk=pk)
        serializer = BookingSerializer(booking, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        booking = get_object_or_404(Booking, pk=pk)
        booking.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)