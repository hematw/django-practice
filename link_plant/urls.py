from django.urls import path
from .views import LinkListView, LinkCreateView, LinkUpdateView, LinkDeleteView, profile_view

urlpatterns = [
    path("", LinkListView.as_view(), name="link_list"),
    path("add-link/", LinkCreateView.as_view(), name="link_plant_add"),
    path("<int:pk>/", LinkUpdateView.as_view(), name="link_plant_update"),
    path("<int:pk>/delete", LinkDeleteView.as_view(), name="link_plant_delete"),
    path("<str:profile_slug>", profile_view, name="profile")
]
