from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="links"),
    path("add-link/", views.add_link, name="add-link"),
    path("<slug:link_slug>/", views.redir_link, name="root_link")
]
