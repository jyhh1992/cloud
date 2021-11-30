from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.open, name='open'),
    path('signup/', views.signup, name='signup'),
    path('login', views.login, name='login'),
    path('home/', views.home, name='home'),
    path('tuto/', views.tuto, name='tuto'),
    path('game/', views.game, name='game'),
    path('record/', views.record, name='record'),
    path('logout/', views.logout, name='logout'),
]  