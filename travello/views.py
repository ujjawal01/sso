from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def news(request):
    return render(request,'news.html')

def home(request):
    return render(request,'Base.html')

