from django.shortcuts import render
from django.http import HttpResponse
def home(request):
    return HttpResponse('I love to go to home')
# Create your views here.
