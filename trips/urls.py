from django.urls import path
from .views import TripsHomeView

urlpatterns = [
    path('', TripsHomeView.as_view(), name='trips-home'),
]
