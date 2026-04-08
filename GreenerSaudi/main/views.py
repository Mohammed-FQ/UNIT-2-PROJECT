from django.shortcuts import render
from django.http import HttpResponse, HttpRequest

def home_view(request: HttpRequest):
    return render(request, 'main/home.html')

def about_view(request: HttpRequest):
    return render(request, 'main/about.html')

def impact_view(request: HttpRequest):
    return render(request, 'main/impact.html')

def progress_view(request: HttpRequest):
    return render(request, 'main/progress.html')

def future_view(request: HttpRequest):
    return render(request, 'main/future.html')

def get_involved_view(request: HttpRequest):
    return render(request, 'main/get_involved.html')

def updates_view(request: HttpRequest):
    return render(request, 'main/updates.html')

def contact_view(request: HttpRequest):
    return render(request, 'main/contact.html')

def base_view(request: HttpRequest):
    return render(request, 'main/base.html')
