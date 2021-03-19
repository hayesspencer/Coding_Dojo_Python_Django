from django.urls import path
from . import views

urlpatterns = [
    path("", views.index),
    path("purchase",views.purchase),
    path("checkout", views.checkout),
]