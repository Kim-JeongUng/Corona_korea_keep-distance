from django.shortcuts import render
from django.http import HttpResponse
from django import template
from corona.GPS_Reader_Saver import get_gps_value
# Create your views here.
def test(request):
<<<<<<< HEAD
    return render(request,'corona/index.html')
=======
    return render(request,'corona/main.html')
>>>>>>> parent of 425b77e8 (update)

def codetest(request):
    return render(request,'corona/read_exel_file.html')

def get_gps(request):
    return render(request,'corona/gps.html')

def get_location(request,user_lng,user_lat):
    return HttpResponse(get_gps_value(user_lng,user_lat))