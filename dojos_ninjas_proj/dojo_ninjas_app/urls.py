from django.urls import path
from . import views

urlpatterns =[
    path('', views.index),
    path('ninjas/create', views.create_ninja),
    path('dojos/create', views.create_dojo),
]