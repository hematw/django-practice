from django.shortcuts import render
from django.views.generic import TemplateView

from .models import Trip
# Create your views here.

class TripsHomeView(TemplateView):
    template_name = "trips/home.html"


def trips_list(req):
    trips = Trip.objects.all()

    context = {
        "trips": trips
    }
    
    return render(req, "trips/trips-list.html", context)