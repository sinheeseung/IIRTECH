from django.urls import path
from . import views


app_name = "dict"


urlpatterns = [
    path('', views.main, name='main'),
    path('searched/', views.search, name='search'),
    path('item/<int:pk>/', views.index, name='item'),
    path('item/<int:pk>/delete/', views.delete, name='delete'),
]
