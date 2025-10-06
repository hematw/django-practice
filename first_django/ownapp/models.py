from django.db import models
from django.utils import timezone

# Create your models here.
class User(models.Model):
    fullname = models.CharField(max_length=64)
    dob = models.DateField(default=timezone.now)
    country= models.CharField(max_length=64)
    email = models.CharField(max_length=64)
    
    def __str__(self):
        return f"{self.fullname} - {self.dob} - {self.country} - {self.email}"
    