from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('search/', views.search_results, name='search'),      
    path('category/<str:category>/', views.category, name='category'),
    path('location/<str:location>/', views.location, name='location'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)