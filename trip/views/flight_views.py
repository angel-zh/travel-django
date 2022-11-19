from django.shortcuts import render, get_object_or_404
from ..serializers import FlightSerializer
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from ..models.flight import Flight


# Create your views here.

# localhost:8000/trip/flights/ ---> get, post

class FlightsView(APIView):
    """View class for flights/ for viewing all and creating a flight trip"""
    serializer_class = FlightSerializer # changes input to form view
    def get(self, request):
        flights = Flight.objects.all()
        serializer = FlightSerializer(flights, many=True)
        return Response({'flights': serializer.data})

    def post(self, request):
        serializer = FlightSerializer(data=request.data)
        # serializer is used as a validation tool and will check to see if incoming data satisfies the fields in our model
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# localhost:8000/trip/flights/:id ---> get, patch, delete

class FlightDetailView(APIView):
    """View class for flights/:pk for viewing, updating, and removing a single flight trip"""
    serializer_class = FlightSerializer
    def get(self, request, pk):
        flight = get_object_or_404(Flight, pk=pk)
        serializer = FlightSerializer(flight)
        return Response({'flight': serializer.data})

    def patch(self, request, pk):
        flight = get_object_or_404(Flight, pk=pk)
        serializer = FlightSerializer(flight, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        flight = get_object_or_404(Flight, pk=pk)
        flight.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
