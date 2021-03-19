from django.urls import path     
from . import views

urlpatterns = [
    path('', views.index),
    path("users/create",views.create_user),
    path("main_page",views.main_page),
    path("users/login",views.login),
    path("logout",views.logout),
    path('giraffes/create', views.create_giraffe),
]