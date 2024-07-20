from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    #return HttpResponse("Welcome buddy!\nYou are at the Home Page of this website.") => simple response
    return render(request, 'website/index.html') # => templating

def about(request):
    return HttpResponse("Welcome buddy!\nYou are at the about Page of this website.")

def contact(request):
    return HttpResponse("Welcome buddy!\nYou are at the contact Page of this website.") 
