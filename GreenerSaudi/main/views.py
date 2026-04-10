from django.http import Http404, HttpRequest
from django.shortcuts import render

from .data import INITIATIVE_BY_SLUG

def home_view(request: HttpRequest):
    return render(request, 'main/home.html')

def about_view(request: HttpRequest):
    return render(request, 'main/about.html')

def impact_view(request: HttpRequest):
    return render(request, 'main/impact.html')

def progress_view(request: HttpRequest):
    return render(request, 'main/progress.html')

def goal_view(request: HttpRequest):
    return render(request, 'main/goal.html')

def get_involved_view(request: HttpRequest):
    return render(request, 'main/get_involved.html')

def news_view(request: HttpRequest):
    return render(request, 'main/news.html')

def contact_view(request: HttpRequest):
    return render(request, 'main/contact.html')

def initiative_detail_view(request: HttpRequest, slug: str):
    initiative = INITIATIVE_BY_SLUG.get(slug)
    if initiative is None:
        raise Http404("Initiative not found")
    return render(request, 'main/initiative_detail.html', {"initiative": initiative})
