from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    return HttpResponse("Hello world")

def auth(request):
    if request.user.is_authenticated:
        return HttpResponse("User is authenticated")
    else:
        return HttpResponse("User is NOT authenticated")