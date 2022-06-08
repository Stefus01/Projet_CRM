from django.shortcuts import render
from .forms import VenueForm
# from .forms import Client

# Create your views here.

def home(request):
	return render(request, 'home_template.html')

def client(request):
	return render(request,'client_template.html')

def add_venue(request):
	form= VenueForm
	return render(request,'add_venue.html',{'form':form})