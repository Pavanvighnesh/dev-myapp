from django.urls import path
from django.contrib import admin
from . import views


urlpatterns=[

    path('',views.index,name='index'),
    path('register',views.register,name='register'),
    path('login',views.login,name='login'),
    
    path('logout',views.logout,name='logout'),
    path('create',views.createrecord,name='create'),
    path('update/<int:pk>',views.updaterecord,name='update'),
    path('delete/<int:pk>',views.deleterecord,name='delete'),
    path('dashboard',views.dashboard.as_view(),name='dashboard'),
   
]