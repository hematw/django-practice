from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import loader
from faker import Faker
import json

from ownapp.models import User
# Create your views here.


def index(request):
    template = loader.get_template("index.html")
    return HttpResponse(template.render())

def about(request):
    return HttpResponse(render(request, "about.html", {"name": "Ghazi"}))

def add_user(request):
    user = User(fullname=Faker().name(), dob=Faker().date_of_birth())
    user.save()
    print("added user",user)
    return HttpResponse(render(request, "user.html", {"user": user}))


def get_users(request):
    users = User.objects.all().values()    
    return HttpResponse(render(request, "users.html", {"users": users}))


def get_user(request, pk):
    # user = User.objects.get(pk=pk)
    
    # we can handle unexpected passed ids here using this function
    # user = get_object_or_404(User, pk=pk, country="Afghanistan 🇦🇫")
    user = get_object_or_404(User, pk=pk)
    context = {
        "profile": user
    } 
    return render(request, "profile.html", context)


def delete_user(request, id):
    print("Id of user", id)
    
    try:
        user = User.objects.get(id=id)
        user.delete()
        return HttpResponse(json.dumps({
            "message": "User deleted",
            "user": user
        }))
    except Exception as e:
        print(e)
        return HttpResponse(json.dumps({"message": "User does not exist"}))
        
        
def notfound(request):
    return HttpResponse("Page not found")