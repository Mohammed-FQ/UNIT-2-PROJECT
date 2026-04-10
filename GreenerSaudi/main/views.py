from django.http import HttpRequest, HttpResponseRedirect
from django.shortcuts import render
from django.utils.http import url_has_allowed_host_and_scheme
from django.views.decorators.http import require_POST


THEME_COOKIE_NAME = 'theme_mode'
DEFAULT_THEME = 'dark'
VALID_THEMES = {'light', 'dark'}


THEME_COOKIE_MAX_AGE = 60 * 60 * 24 * 365


def normalize_theme(theme_value: str | None) -> str:
    if theme_value in VALID_THEMES:
        return theme_value
    return DEFAULT_THEME


def render_page(request: HttpRequest, template_name: str, context: dict | None = None):
    page_context = {'theme_mode': normalize_theme(request.COOKIES.get(THEME_COOKIE_NAME))}
    if context:
        page_context.update(context)
    return render(request, template_name, page_context)

def home_view(request: HttpRequest):
    return render_page(request, 'main/home.html')

def about_view(request: HttpRequest):
    return render_page(request, 'main/about.html')

def impact_view(request: HttpRequest):
    return render_page(request, 'main/impact.html')

def progress_view(request: HttpRequest):
    return render_page(request, 'main/progress.html')

def goal_view(request: HttpRequest):
    return render_page(request, 'main/goal.html')

def get_involved_view(request: HttpRequest):
    return render_page(request, 'main/get_involved.html')

def news_view(request: HttpRequest):
    return render_page(request, 'main/news.html')

def contact_view(request: HttpRequest):
    return render_page(request, 'main/contact.html')


@require_POST
def set_theme_view(request: HttpRequest):
    current_theme = normalize_theme(request.COOKIES.get(THEME_COOKIE_NAME))
    requested_theme = request.POST.get('theme')

    if requested_theme not in VALID_THEMES:
        requested_theme = 'dark' if current_theme == 'light' else 'light'

    next_url = request.POST.get('next') or request.META.get('HTTP_REFERER') or '/'
    if not url_has_allowed_host_and_scheme(
        url=next_url,
        allowed_hosts={request.get_host()},
        require_https=request.is_secure(),
    ):
        next_url = '/'

    response = HttpResponseRedirect(next_url)
    response.set_cookie(
        THEME_COOKIE_NAME,
        requested_theme,
        max_age=THEME_COOKIE_MAX_AGE,
        samesite='Lax',
    )
    return response
