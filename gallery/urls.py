from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('search/', views.search_results, name='search'),      
    path('', views.category, name='category'),
    path('', views.location, name='location'),
]