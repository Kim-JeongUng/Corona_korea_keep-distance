from django.urls import path
from . import views
from django.conf.urls import url
urlpatterns = [
    path('', views.index, name='login'),
    path('news/<str:query>',views.get_news,name="news"),
    path('gps/', views.get_gps, name="get_gps_value"),
    path('gps/<str:user_lng>/<str:user_lat>', views.get_location, name="get_location"),
    path('jenan/<str:area>',views.jenan,name="jenan"),
    path('calendar/', views.CalendarView.as_view(), name='calendar'),
    url(r'^event/new/$', views.event, name='event_new'),
    url(r'^event/edit/(?P<event_id>\d+)/$', views.event, name='event_edit'),
    path('lg/',views.users_login,name='lg'),
]