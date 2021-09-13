from django.urls import path
from . import views
urlpatterns = [
    path('',views.test,name='index'),
    path('python/', views.codetest, name='pythoncodetest'),
    path('gps/',views.get_gps,name='get_gps_value'),
]