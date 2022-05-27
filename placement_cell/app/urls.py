from django.urls import path
from . import views


urlpatterns = [
    path('', views.login, name='home'),
    path('signup', views.home, name='home'),
    path('login', views.login, name='login'),
    path('addcompany', views.company, name='company'),
    path('apply', views.apply, name='apply'),
    path('download', views.download, name='download'),

    
       
]