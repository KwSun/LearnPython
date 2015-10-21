from django.shortcuts import render
from django.http.response import HttpResponse

# Create your views here.


def index(request):
    return HttpResponse('index')

def lists(request,id,name):
    print id,name
    return HttpResponse('list')