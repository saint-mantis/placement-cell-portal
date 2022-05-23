from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('home', views.home, name='home'),
    path('login', views.login, name='login'),
    path('addcompany', views.company, name='company'),
    path('apply', views.apply, name='apply'),

    
       
]