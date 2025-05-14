from django.shortcuts import render, HttpResponse

# Create your views here.


def menu_list(request):
    return HttpResponse('Welcome to Menu Items:')
