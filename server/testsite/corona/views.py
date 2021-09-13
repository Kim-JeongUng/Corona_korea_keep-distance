from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def test(request):
    return render(request,'corona/index.html')

def codetest(request):
    return render(request,'corona/read_exel_file.html')

def get_gps(request):
    return render(request,'corona/gps.html')