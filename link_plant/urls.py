from django.urls import path
from .views import LinkListView, LinkCreateView

urlpatterns = [
    path("", LinkListView.as_view(), name="link_list"),
    path("add-link/", LinkCreateView.as_view(), name="link_plant_add")
]
