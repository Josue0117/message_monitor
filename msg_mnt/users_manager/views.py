from django.contrib.auth.models import User
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from users_manager.forms import ProfileForm, SignupForm


def index(request):
    return render(request,"index.html",{"home":"active"})


def mis_conversaciones(request):
    return render(request,"index.html",{"login":"active"})


def sbr_conversaciones(request):
    return render(request,"index.html",{"login":"active"})


def profile_form(request):
    if request.method == 'POST':
        form=ProfileForm(request.POST)

        if form.is_valid():
            form.save()
            return render(request,"index.html",{"home":"active"})

    else:
        form=ProfileForm()
    return render(request,"profile-form.html",{"login":"active", "form":form})


def login(request):
    if request.method == 'POST':
        form=ProfileForm(request.POST)

        if form.is_valid():
            form.save()
            return render(request,"index.html",{"home":"active"})

    else:
        form=ProfileForm()

    return render(request,"login.html",{"login":"active","form":form})


class User_register(CreateView):
    model=User
    template_name="new_login.html"
    form_class=SignupForm
    success_url=reverse_lazy("profile-form")