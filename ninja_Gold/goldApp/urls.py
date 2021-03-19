from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('reset', views.reset),
    path('gold', views.process_gold)
]