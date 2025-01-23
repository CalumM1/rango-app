from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Welcome to the index page! Click <a href='/rango/about/'> HERE </a> to go to about.")

def about(request):
    return HttpResponse("Welcome to the about page! Click <a href='http:/rango/'> HERE </a> to go to the index page.")