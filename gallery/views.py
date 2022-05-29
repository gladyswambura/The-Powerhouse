from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import Image, Category, Location


# Create your views here.
def index(request):
    try:
        images = Image.objects.all()
        category = Category.objects.all()
        location = Location.objects.all()
    except Image.DoesNotExist:
        raise Http404() 
    return render(request,'index.html', {'images':images,'location':location,'category':category})

def about(request):
    return render (request,'about.html')

def search_results(request):
    if 'category' in request.GET and request.GET["category"]:
        search_term = request.GET.get("category")
        searched_category = Category.search_by_category(search_term)
        message = f"{search_term}"

        return render(request, 'search.html',{"message":message,"categories":searched_category})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})
    
def search_location(request):
    if 'category' in request.GET and request.GET["category"]:
        search_term = request.GET.get("category")
        searched_category = Category.search_by_category(search_term)
        message = f"{search_term}"

        return render(request, 'search.html',{"message":message,"categories":searched_category})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})
    

def category(request, category):
    category_results = Category.objects.all()
    location_results = Location.objects.all()
    category_result = Image.objects.filter(image_category__category_name = category)
    message = f"{category}"
    return render(request,'index.html',{"message":message,'all_images':category_result,'category_results':category_results,'location_results':location_results})

def location(request, location):
    category_results = Category.objects.all()
    location_results = Location.objects.all()
    location_result = Image.objects.filter(image_location__location_name= location)
    message = f"{location}"
    return render(request,'index.html',{"message":message,'all_images':location_result,'category_results':category_results,'location_results':location_results})





