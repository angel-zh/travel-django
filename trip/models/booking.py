from django.db import models
from .flight import Flight
from .hotel import Hotel

class Booking(models.Model):
    flight = models.ForeignKey(
        Flight,
        on_delete=models.CASCADE
    ) 
    traveller = models.ForeignKey(
        'Traveller',
        on_delete=models.CASCADE
    )
    hotel = models.ForeignKey(
        'Hotel',
        on_delete=models.CASCADE
    )
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Created on {self.created_at}"