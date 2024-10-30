from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return HttpResponse('anasayfa')

def kurslar(request):
    return HttpResponse("kurs listesi")
# Create your views here.
