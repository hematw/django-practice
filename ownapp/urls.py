from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="home"),
    path("users/", views.get_users, name="users"),
    path("users/<int:pk>/", views.get_user, name="users"),
    path("add-user/", views.add_user, name="add-user"),
    path("delete-user/<int:id>", views.delete_user, name="del-user"),
    path("about/", views.about, name="about"),
    path("*", views.notfound),
]
