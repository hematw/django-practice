from django.shortcuts import render, redirect, get_object_or_404
from .models import Link
from .forms import LinkForm


# Create your views here.
def index(request):
    links = Link.objects.all()
    context = {
        "links": links
    }
    
    print(context)
    return render(request, "links/index.html", context)

def add_link(request):
    # print(request.POST)
    if request.method == "POST" :
        linkform = LinkForm(request.POST)
        if linkform.is_valid():
            print(linkform.cleaned_data)
            linkform.save()
            return redirect("/links")
        
    else:
        linkform = LinkForm()
    context = {
        "form": linkform
    }
    return render(request, "links/add_link.html", context)

def redir_link(request, link_slug):
    # link = Link.objects.get_object_or
    link = get_object_or_404(Link, slug=link_slug)
    link.click()
    return redirect(link.url)