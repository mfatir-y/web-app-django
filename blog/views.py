from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse('blog/home.html')

def about(request):
    return HttpResponse('blog/about.html')
