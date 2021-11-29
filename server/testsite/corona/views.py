
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django import template
from django.template import RequestContext

from django.db import connection
from corona.GPS_Reader_Saver import get_gps_value
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout

from django.contrib.auth import login
from django.urls import reverse
from django.contrib.auth import authenticate
from datetime import datetime,date,timedelta
from django.views import generic
from django.utils.safestring import mark_safe
from .models import Event
from .utils import Calendar
import calendar
from .forms import EventForm
from corona.GPS_Reader_Saver import get_gps_value
from corona.NewsCrawling_test import news
from corona.JenanMessage import jenan_area
from corona.governmentNews import gnews
# Create your views here.


def register(request):   #회원가입 페이지를 보여주기 위한 함수
    if request.method == "GET":
        return render(request, 'corona/register.html')
    elif request.method == "POST":
        username = request.POST.get('username',None)   #딕셔너리형태
        password = request.POST.get('password',None)
        re_password = request.POST.get('re_password',None)
        res_data = {}
        if not (username and password and re_password) :
            res_data['error'] = "모든 값을 입력해야 합니다."
            return render(request, 'corona/register.html',res_data)
        if password != re_password :
            # return HttpResponse('비밀번호가 다릅니다.')
            res_data['error'] = '비밀번호가 다릅니다.'
            return render(request, 'corona/register.html', res_data)
        else :
            user = User(username=username, password=make_password(password))
            user.save()
            return redirect(reverse('lg'))

def users_login(request):
    if  request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(username=username, password=password)
        if user is not None:
            print("인증성공")
            #login(request, user)
            return redirect(reverse('login'))
        else:
            print("인증실패")
    return render(request, "corona/user_login.html")

def users_logout(request):
    logout(request)
    return redirect("users:login")

class CalendarView(generic.ListView):
    model = Event
    template_name = 'corona/calendar.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        d = get_date(self.request.GET.get('month', None))
        cal = Calendar(d.year, d.month)
        html_cal = cal.formatmonth(withyear=True)
        context['calendar'] = mark_safe(html_cal)
        context['prev_month'] = prev_month(d)
        context['next_month'] = next_month(d)
        return context

def get_date(req_month):
    if req_month:
        year, month = (int(x) for x in req_month.split('-'))
        return date(year, month, day=1)
    return datetime.today()

def prev_month(d):
    first = d.replace(day=1)
    prev_month = first - timedelta(days=1)
    month = 'month=' + str(prev_month.year) + '-' + str(prev_month.month)
    return month

def next_month(d):
    days_in_month = calendar.monthrange(d.year, d.month)[1]
    last = d.replace(day=days_in_month)
    next_month = last + timedelta(days=1)
    month = 'month=' + str(next_month.year) + '-' + str(next_month.month)
    return month

def event(request, event_id=None):
    instance = Event()
    if event_id:
        instance = get_object_or_404(Event, pk=event_id)
    else:
        instance = Event()

    form = EventForm(request.POST or None, instance=instance)
    if request.POST and form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('calendar'))
    return render(request, 'corona/event.html', {'form': form})



def get_news(request,query):
    return HttpResponse(news(query))

def get_gnews(request):
    return HttpResponse(gnews())

def jenan(request,area):
    return HttpResponse(jenan_area(area))

def index(request):
    return render(request,'corona/index.html')

def news_page(request):
    return render(request,'corona/news_page.html')

def gnews_page(request):
    return render(request,'corona/gnews_page.html')

def get_gps(request):
    return render(request,'corona/gps.js')

def get_location(request,user_lng,user_lat):
    return HttpResponse(get_gps_value(user_lng,user_lat))