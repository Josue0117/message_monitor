from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from users_manager.forms import SignupForm

def index(request):
    return render(request,"index.html",{"home":"active"})

def mis_conversaciones(request):
    return render(request,"index.html",{"login":"active"})

def sbr_conversaciones(request):
    return render(request,"index.html",{"login":"active"})

def login(request):
    if request.method == 'POST':
        form=SignupForm(request.POST)

        if form.is_valid():
            form.save()
            return render(request,"index.html",{"home":"active"})

    else:
        form=SignupForm()

    return render(request,"login.html",{"login":"active","form":form})