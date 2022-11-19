from django.urls import path
from .views.hotel_views import HotelsView, HotelDetailView
from .views.flight_views import FlightsView, FlightDetailView
from .views.traveller_views import TravellersView, TravellerDetailView
from .views.booking_views import BookingsView, BookingDetailView

urlpatterns = [
    path('hotels/', HotelsView.as_view(), name='hotels'),
    path('hotels/<int:pk>/', HotelDetailView.as_view(), name='hotel'),
    path('flights/', FlightsView.as_view(), name='flights'),
    path('flights/<int:pk>/', FlightDetailView.as_view(), name='flight'),
    path('travellers/', TravellersView.as_view(), name='travellers'),
    path('travellers/<int:pk>/', TravellerDetailView.as_view(), name='traveller'),
    path('bookings/', BookingsView.as_view(), name='bookings'),
    path('bookings/<int:pk>/', BookingDetailView.as_view(), name='booking'),
]