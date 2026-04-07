from django.shortcuts import render
from django.http import HttpResponse, HttpRequest

def home_view(request: HttpRequest):
    return render(request, 'main/home.html')

def base_view(request: HttpRequest):
    return render(request, 'main/base.html')
