from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    # construct dictionary to pass to template engine
    context_dict = {'boldmessage': 'crunchy, creamy, cookie, candy, cupcake!'}

    # run rendered response to send to client
    return render(request, 'rango/index.html', context=context_dict)

def about(request):

    context_dict = {'boldmessage': 'This tutorial was put together by Calum.'}

    return render(request, 'rango/about.html', context=context_dict)