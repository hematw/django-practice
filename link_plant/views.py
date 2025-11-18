from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import LinkP, Profile
from django.urls import reverse_lazy

# Create your views here.

class LinkListView(ListView):
    model= LinkP
    
    
class LinkCreateView(CreateView):
    model=LinkP
    fields="__all__"
    # success_url="/link-plant"
    success_url = reverse_lazy("link_list")
    
    
class LinkUpdateView(UpdateView):
    model = LinkP
    fields = ["text", "url"]
    success_url = reverse_lazy("link_list")
    

class LinkDeleteView(DeleteView):
    model=LinkP
    success_url = reverse_lazy("link_list")
    

def profile_view(request, profile_slug):
    profile = get_object_or_404(Profile, slug=profile_slug)
    links = profile.links.all()
    
    context = {
        "profile":profile,
        "links": links
    }
    
    return render(request, "link_plant/profile.html", context)