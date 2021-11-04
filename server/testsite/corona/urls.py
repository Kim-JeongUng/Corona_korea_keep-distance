from django.urls import path
from . import views

urlpatterns = [
    path('python/', views.codetest, name='pythoncodetest'),
    path('', views.index, name='login'),
    path('news/<str:query>',views.get_news,name="news"),
    path('gps/', views.get_gps, name="get_gps_value"),
    path('gps/<str:user_lng>/<str:user_lat>', views.get_location, name="get_location"),
]