from django.shortcuts import render
from django.http import HttpResponse

def index(type):
    if 'id' in type.GET:
        text = type.GET['id']
    else:
        text = 'Hello World!!!'
    return HttpResponse(text)
