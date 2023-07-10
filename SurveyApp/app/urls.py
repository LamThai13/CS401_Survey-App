from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('ratehome/', views.ratehome, name='ratehome'),
    path('create/',views.create, name='create'),
    path('createRate/',views.createRating, name='createRate'),
    path('vote/<poll_id>/',views.vote, name='vote'),
    path('result/<poll_id>/',views.result, name='result'),
    path('register/',views.register, name='register'),
    path('login/',views.loginPage, name='login'),
    path('logout/',views.logoutPage, name='logout'),
]