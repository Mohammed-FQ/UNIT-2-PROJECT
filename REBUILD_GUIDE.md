# Rebuilding Greener Saudi Step by Step

This guide is for rebuilding this project yourself from the beginning, with short explanations for what each step does.

The project is a Django website with:

- one Django project: `GreenerSaudi`
- one main app: `main`
- multiple pages using template inheritance
- shared static files for CSS, images, JS, and video
- light/dark mode using a cookie

---

## 1. Decide the website idea and page plan

Before coding, decide the topic and pages.

For this project, the idea is:

- topic: Saudi Green Initiative
- purpose: explain the initiative, show impact, show progress, and encourage involvement

Page plan used here:

- Home
- About
- Impact
- Progress
- Goal
- Get Involved
- News
- Contact

Why this step matters:

- It keeps the project coherent.
- It helps you meet the requirement of home page + at least 6 pages.

---

## 2. Create the Django project and app

Run these commands:

```bash
django-admin startproject GreenerSaudi
cd GreenerSaudi
python manage.py startapp main
```

What this does:

- `startproject` creates the main Django configuration.
- `startapp` creates the app where your pages, urls, and templates will live.

---

## 3. Register the app in settings

Open `GreenerSaudi/settings.py` and add `main` to `INSTALLED_APPS`.

You also need the request context processor, because this project uses `request.COOKIES` inside templates for dark mode.

Important parts in this project:

- `INSTALLED_APPS` includes `main`
- templates use `APP_DIRS = True`
- context processors include `django.template.context_processors.request`

Why this step matters:

- Without adding `main`, Django will not load your app templates and files correctly.
- Without the request context processor, dark mode checking in the template will not work.

---

## 4. Connect project urls to the app

In `GreenerSaudi/urls.py`, include the app urls:

```python
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
]
```

What this does:

- It tells Django to send all website routes to `main/urls.py`.

---

## 5. Create the app urls

In `main/urls.py`, define one route for each page.

This project uses:

```python
urlpatterns = [
    path('', views.home_view, name='home_view'),
    path('mode/<mode>/', views.mode_view, name='mode_view'),
    path('about/', views.about_view, name='about_view'),
    path('impact/', views.impact_view, name='impact_view'),
    path('progress/', views.progress_view, name='progress_view'),
    path('goal/', views.goal_view, name='goal_view'),
    path('get-involved/', views.get_involved_view, name='get_involved_view'),
    path('news/', views.news_view, name='news_view'),
    path('contact/', views.contact_view, name='contact_view'),
]
```

Why this step matters:

- This is the map of your website.
- Named urls make template links easier with `{% url %}`.

---

## 6. Create simple views first

In `main/views.py`, start with basic render views.

Example from this project:

```python
from django.http import HttpRequest
from django.shortcuts import redirect, render


def home_view(request: HttpRequest):
    return render(request, 'main/home.html')
```

Then repeat the same pattern for the rest of the pages.

Why this step matters:

- It gets the site working early.
- You can build the design page by page after the routing is done.

---

## 7. Add the dark mode view

This project uses a very simple cookie-based dark mode.

In `main/views.py`:

```python
def mode_view(request: HttpRequest, mode: str):
    response = redirect(request.GET.get('next', '/'))

    if mode == 'light':
        response.set_cookie('mode', 'light')
    elif mode == 'dark':
        response.set_cookie('mode', 'dark')

    return response
```

What this does:

- It reads the mode from the url.
- It saves the selected theme in a cookie.
- It redirects the user back to the page they were on.

Why this is nice for a class project:

- It is simple.
- It uses Django views and urls directly.
- It matches the way you were taught better than a more complicated setup.

---

## 8. Create the template and static folder structure

Inside the `main` app, create these folders:

```text
main/
  templates/
    main/
      base.html
      home.html
      about.html
      impact.html
      progress.html
      goal.html
      get_involved.html
      news.html
      contact.html
  static/
    css/
    img/
    js/
    videos/
    bootstrap/
    fonts/
```

Why this step matters:

- Django looks for templates inside `templates/app_name/`.
- Static files stay organized and easier to reuse.

---

## 9. Build `base.html` first

This is the most important template in the project.

`base.html` contains:

- the HTML skeleton
- font links
- Bootstrap CSS and JS
- your custom stylesheet
- navbar
- hero section
- footer
- dark mode button
- template blocks for child pages

Key idea:

- every other page extends `base.html`

Important blocks used in this project:

- `{% block title %}`
- `{% block hero_image %}`
- `{% block hero_title %}`
- `{% block hero_subtitle %}`
- `{% block hero_media %}`
- `{% block content %}`

Why this step matters:

- It keeps the whole site uniform.
- You only build the navbar/footer once.

---

## 10. Make the hero section reusable

In this project, each page changes the hero by overriding blocks in `base.html`.

Example idea:

```django
{% block hero_image %}{% static 'img/mangroves.webp' %}{% endblock %}
{% block hero_title %}About the Initiative{% endblock %}
```

What this does:

- Each page gets its own background image and title.
- You keep one consistent hero structure across the whole site.

---

## 11. Build the home page first

The home page is the summary page of the whole website.

In this project, `home.html`:

- extends `base.html`
- uses a video hero
- contains three main sections
- links to the other pages

Good way to rebuild it:

1. Add the hero.
2. Add the first section introducing the initiative.
3. Add the second section for progress and goals.
4. Add the final section linking to involvement, news, and contact.

Why this step matters:

- Once the home page is done, the visual language of the whole site becomes clear.

---

## 12. Create one content page and reuse the same pattern

After Home, build one strong content page like `about.html`.

Use repeated building blocks such as:

- `image-section`
- `section-shell`
- `section-panel`
- `section-heading`
- `section-lead`
- `stat-card`

Then reuse the same structure for the other pages.

Why this step matters:

- It saves time.
- It keeps the design consistent.
- You do not need to invent a new layout for every page.

---

## 13. Write the shared CSS in `style.css`

This project depends heavily on shared CSS classes.

Main jobs of `style.css`:

- define light/dark theme variables
- style the navbar and footer
- style hero sections
- create reusable section backgrounds
- style cards, headings, spacing, and buttons
- help responsiveness

The most important pattern is the CSS variables setup:

```css
:root {
  --site-body-bg: #f5f2ea;
  --site-body-color: #151515;
}

[data-bs-theme="dark"] {
  --site-body-bg: #0d1615;
  --site-body-color: #edf1ee;
}
```

What this does:

- Light mode uses one set of colors.
- Dark mode swaps the variables without rewriting every rule.

---

## 14. Connect dark mode in the template

In `base.html`, the `<html>` element checks the cookie:

```django
<html data-bs-theme="{% if 'mode' in request.COOKIES and request.COOKIES.mode == 'dark' %}dark{% else %}light{% endif %}" lang="en">
```

And the footer button links to the mode view.

What this does:

- If the cookie says `dark`, dark colors are used.
- If not, the page uses light mode.

---

## 15. Add images, video, and other static files

Put your assets into `main/static/`.

Examples used in this project:

- images in `main/static/img/`
- CSS in `main/static/css/`
- JS in `main/static/js/`
- video in `main/static/videos/`

Why this step matters:

- Django serves static files separately from templates.
- You can reference them with `{% static '...' %}`.

---

## 16. Add animation carefully

This project uses AOS and animate.css.

They are loaded in `base.html`, and many sections use attributes like:

```html
data-aos="fade-right"
data-aos-duration="700"
```

Why to be careful:

- animations can cause layout issues on smaller screens
- too much movement can make the page feel messy

Good rule:

- add animation after the layout already works

---

## 17. Build the remaining pages one by one

Recommended order:

1. Home
2. About
3. Impact
4. Progress
5. Goal
6. Get Involved
7. News
8. Contact

Small explanation:

- Start with core information pages first.
- Leave lighter pages like News and Contact until the structure is already stable.

---

## 18. Check responsiveness after each major page

Do not wait until the end.

After building each page, test:

- desktop
- laptop width
- tablet width
- phone width

Things to watch for:

- horizontal scrolling
- headings becoming too wide
- cards stacking badly
- navbar collapsing correctly
- video or images overflowing

Why this step matters:

- Responsive issues are easier to fix early.

---

## 19. Run the project often while rebuilding

Use:

```bash
python manage.py runserver
```

Open the local site and test each page as you build.

Why this step matters:

- You catch broken links and template mistakes immediately.

---

## 20. Final checklist before calling it done

Use this checklist:

- Django project runs without errors
- all pages open from the navbar
- home page + at least 6 more pages exist
- templates use inheritance
- static files are working
- dark mode and light mode both work
- layout is responsive
- design feels consistent across all pages

---

## Suggested rebuild order for this exact project

If you want to rebuild this exact site with less confusion, follow this order exactly:

1. Create project and app.
2. Set up `settings.py` and `urls.py`.
3. Create basic render views.
4. Create empty templates for all pages.
5. Build `base.html`.
6. Build `style.css` with theme variables and shared classes.
7. Add dark mode cookie view and footer button.
8. Build the home page.
9. Build About using the same layout pattern.
10. Reuse the same pattern for Impact, Progress, Goal, and Get Involved.
11. Add News and Contact last.
12. Do one full responsive pass.

This order works well because each step depends on the one before it.

---

## The main idea to remember

This project is not a lot of separate complicated pieces.

It is mostly just these 5 ideas repeated well:

1. urls send requests to views
2. views render templates
3. all pages extend one `base.html`
4. shared CSS classes create a consistent design
5. dark mode works by switching a cookie and reading it in the template

If you understand those 5 ideas, rebuilding the project becomes much easier.