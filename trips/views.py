from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.


class TripsHomeView(TemplateView):
    template_name = "trips/home.html"