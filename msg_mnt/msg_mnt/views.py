from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,"index.html",{"home":"active"})

def mis_conversaciones(request):
    return render(request,"index.html",{"login":"active"})

def sbr_conversaciones(request):
    return render(request,"index.html",{"login":"active"})

def login(request):
    return render(request,"login.html",{"login":"active"})