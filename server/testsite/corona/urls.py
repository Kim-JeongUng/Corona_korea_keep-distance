from django.urls import path
from . import views

urlpatterns = [
    path('',views.test,name='index'),
    path('python/', views.codetest, name='pythoncodetest'),
    path('gps/',views.get_gps,name="get_gps_value"),
    path('gps/<str:user_lng>/<str:user_lat>',views.get_location,name="get_location"),
    path('login/',views.login,name='login'),
    path('test/',views.test,name='test'),
    path('test/',views.Login),
    path('news/<str:query>',views.get_news,name="news")
]