from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator

# Create your models here.


class Trip(models.Model):
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="trips")

    def __str__(self):
        return f"{self.city}, {self.country}"


class Note(models.Model):
    TYPE_CHOICES = (
        ("plan", "Plan"),
        ("activity", "Activity"),
        ("rest", "Rest"),
    )

    trip = models.ForeignKey(Trip, on_delete=models.CASCADE, related_name="notes")
    name = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    type = models.CharField(max_length=100, choices=TYPE_CHOICES)
    img = models.ImageField(upload_to="trip_notes/", blank=True, null=True)
    rating = models.PositiveSmallIntegerField(
        default=1, validators=[MaxValueValidator(5)]
    )

    def __str__(self):
        return f"{self.name} in {self.trip.city}"
