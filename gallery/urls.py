from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:gallery_id>/', views.detail, name='detail'),
    path('<int:gallery_id>/<int:image_id>/', views.image, name='image'),
]