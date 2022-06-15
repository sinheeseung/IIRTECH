from django.urls import path
from . import views


app_name = "dict"


urlpatterns = [
    #path('', views.index, name='index'),
    path('', views.main, name='main'),
    path('searched/', views.search, name='search'),
]
