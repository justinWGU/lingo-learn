from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated


# Create your views here.
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def index(request):
    return HttpResponse("Hello world")
