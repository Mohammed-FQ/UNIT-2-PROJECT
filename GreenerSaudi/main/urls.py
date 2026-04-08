from django.urls import path
from . import views 


app_name ='main'
urlpatterns = [
    path('', views.home_view, name='home_view'),
    path('about/', views.about_view, name='about_view'),
    path('impact/', views.impact_view, name='impact_view'),
    path('progress/', views.progress_view, name='progress_view'),
    path('future/', views.future_view, name='future_view'),
    path('get-involved/', views.get_involved_view, name='get_involved_view'),
    path('updates/', views.updates_view, name='updates_view'),
    path('contact/', views.contact_view, name='contact_view'),
    path('base/', views.base_view, name='base_view'),
]

