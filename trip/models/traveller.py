from django.db import models
from .flight import Flight
from .booking import Booking
from .hotel import Hotel

class Traveller(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    citizenship = models.CharField(max_length=100)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    booked_flights = models.ManyToManyField(
        Flight,
        through=Booking,
        through_fields=('traveller', 'flight')
    )
    booked_hotels = models.ManyToManyField(
        Hotel,
        through=Booking,
        through_fields=('traveller', 'hotel')
    )

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
