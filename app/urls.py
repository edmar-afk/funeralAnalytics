from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
    path('login/', views.userLogin, name='login'),
    path('homepage', views.homepage, name='homepage'), 
    path('chart', views.chart, name='chart'),
    path('logout', views.userLogout, name='logout'),  # Use custom logout view
]
