from django.db import models

# Create your models here.
class Flight(models.Model):
    airline = models.CharField(max_length=50)
    flight_number = models.CharField(max_length=10)
    departure_airport = models.CharField(max_length=10)
    arrival_airport = models.CharField(max_length=10)
    scheduled_time = models.DateTimeField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.flight_number
