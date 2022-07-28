from django.shortcuts import render

# Create your views here.
from django.template import loader

def login(request): 
    return render (request,"login.html",{})

def doLogin(request): 
    return render (request,"home.html",{})

def blank(request): 
    return render (request,"blank.html",{})



