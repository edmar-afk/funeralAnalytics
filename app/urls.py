from django.urls import path, include
from . import views

urlpatterns = [
    path('homepage', views.homepage, name='homepage'), 
    path('chart', views.chart, name='chart'),

]