from django.shortcuts import render
from django.http import HttpResponse
from django import template
from .models import Login
from django.db import connection
from corona.GPS_Reader_Saver import get_gps_value
from corona.NewsCrawling_test import news
# Create your views here.
def test(request):
    return render(request,'corona/main.html')

def codetest(request):
    return render(request,'corona/read_exel_file.html')

def get_gps(request):
    return render(request,'corona/gps.html')

def get_news(request,query):
    return HttpResponse(news(query))

def index(request):
    return render(request,'corona/index.html')

def logindb(request):
    login=Login.objects.all()
    data={'login':login}
    return render(request, 'corona/test.html',data)

def get_location(request,user_lng,user_lat):
    return HttpResponse(get_gps_value(user_lng,user_lat))