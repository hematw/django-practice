from django.shortcuts import render
from .models import Link

# Create your views here.
def index(request):
    links = Link.objects.all()
    context = {
        "links": links
    }
    
    print(context)
    return render(request, "links/index.html", context)