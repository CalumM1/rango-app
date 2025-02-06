from django.shortcuts import render
from rango.models import Category
from django.http import HttpResponse

def index(request):
    category_list = Category.objects.order_by('-likes')[:5]

    context_dict = {}
    context_dict["boldmessage"] = 'Crunchy, creamy, cookie, candy, cupcake!'
    context_dict["categories"] = category_list

    return render(request, 'rango/index.html', context=context_dict)

def about(request):

    context_dict = {'boldmessage': 'This tutorial has been put together by Calum.'}

    return render(request, 'rango/about.html', context=context_dict)