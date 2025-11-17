from django.shortcuts import render
from django.views.generic import ListView, CreateView
from .models import LinkP

# Create your views here.

class LinkListView(ListView):
    model= LinkP
    
    
class LinkCreateView(CreateView):
    model=LinkP
    fields="__all__"
    success_url="/link-plant"