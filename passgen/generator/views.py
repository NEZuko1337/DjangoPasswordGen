from django.shortcuts import render
from django.http import HttpResponse
import random


def home(request):
    return render(request, "generator/home.html")


def password(request):
    characters = list('qwertyuiopasdfghjklzxcvbnm')
    if request.GET.get('uppercase'):
        characters.extend(list("QWERTYUIOPASDFGHJKLZXCVBNM"))
    len = int(request.GET.get('length', 8))
    if request.GET.get('special'):
        characters.extend(list("!@#$%^&*()_-+=)"))
    if request.GET.get('numbers'):
        characters.extend(list("1234567890"))

    passw = ""
    for x in range(len):
        passw += random.choice(characters)
    return render(request, "generator/password.html", {'password': passw})


def about(request):
    return render(request, "generator/about.html")