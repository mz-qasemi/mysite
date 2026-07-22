from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index_view(request):
    return HttpResponse("<H1>Home Page</H1>")

def about_view(request):    
    return HttpResponse("<H1>About Page</H1>")

def contact_view(request):    
    return HttpResponse("<H1>Contact Page<H1>")