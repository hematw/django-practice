from django.conf import settings
from django.urls import path
from .views import TripsHomeView
from django.conf import settings
from django.conf.urls.static import static
from .views import trips_list

urlpatterns = [
    path('', TripsHomeView.as_view(), name='trips-home'),
    path("trips-list/", trips_list, name="trips-list")
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
