from django.shortcuts import render, get_object_or_404
from ..serializers import TravellerSerializer
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from ..models.traveller import Traveller


# Create your views here.

# localhost:8000/trip/travellers/ ---> get, post

class TravellersView(APIView):
    """View class for travellers/ for viewing all and creating a traveller trip"""
    serializer_class = TravellerSerializer
    def get(self, request):
        travellers = Traveller.objects.all()
        serializer = TravellerSerializer(travellers, many=True)
        return Response({'travellers': serializer.data})

    def post(self, request):
        serializer = TravellerSerializer(data=request.data)
        # serializer is used as a validation tool and will check to see if incoming data satisfies the fields in our model
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# localhost:8000/trip/travellers/:id ---> get, patch, delete

class TravellerDetailView(APIView):
    """View class for travellers/:pk for viewing, updating, and removing a single traveller trip"""
    serializer_class = TravellerSerializer
    def get(self, request, pk):
        traveller = get_object_or_404(Traveller, pk=pk)
        serializer = TravellerSerializer(traveller)
        return Response({'traveller': serializer.data})

    def patch(self, request, pk):
        traveller = get_object_or_404(Traveller, pk=pk)
        serializer = TravellerSerializer(traveller, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        traveller = get_object_or_404(Traveller, pk=pk)
        traveller.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
