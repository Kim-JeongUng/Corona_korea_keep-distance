from django.urls import path
from . import views
urlpatterns = [
    path('',views.test,name='index'),
    path('python/', views.codetest, name='pythoncodetest'),
<<<<<<< HEAD
<<<<<<< HEAD
    path('gps/',views.get_gps,name="get_gps_value"),
    path('gps/<str:user_lng>/<str:user_lat>',views.get_location,name="get_location"),
=======
    path('test/',views.test,name='test'),
    path('', views.index, name='login'),
    path('news/<str:query>',views.get_news,name="news"),
    path('gps/', views.get_gps, name="get_gps_value"),
    path('gps/<str:user_lng>/<str:user_lat>', views.get_location, name="get_location"),
>>>>>>> parent of 425b77e8 (update)
=======
    path('gps/',views.get_gps,name="get_gps_value"),
    path('gps/<str:user_lng>/<str:user_lat>',views.get_location,name="get_location"),
>>>>>>> parent of 29aae208 (11/4)
]