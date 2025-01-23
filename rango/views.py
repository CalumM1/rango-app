from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Welcome to the index page! Click <a href='http://127.0.0.1:8000/rango/about/'> HERE </a> to go to about.")

def about(request):
    return HttpResponse("Welcome to the about page! Click <a href='http://127.0.0.1:8000/rango/'> HERE </a> to go to the index page.")