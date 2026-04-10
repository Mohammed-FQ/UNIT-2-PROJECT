from django.urls import path
from . import views 


app_name ='main'
urlpatterns = [
    path('', views.home_view, name='home_view'),
    path('about/', views.about_view, name='about_view'),
    path('impact/', views.impact_view, name='impact_view'),
    path('progress/', views.progress_view, name='progress_view'),
    path('goal/', views.goal_view, name='goal_view'),
    path('get-involved/', views.get_involved_view, name='get_involved_view'),
    path('news/', views.news_view, name='news_view'),
    path('contact/', views.contact_view, name='contact_view'),
    path('initiative/<slug:slug>/', views.initiative_detail_view, name='initiative_detail_view'),
]

