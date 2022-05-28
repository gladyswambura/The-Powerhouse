from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    return render(request, 'base.html')

def search_results(request):
    return render(request, 'search.html')

def category(request):
    return render(request, 'base.html')

def location(request):
    return render(request, 'base.html')






