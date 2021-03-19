from django.urls import path     
from . import views

urlpatterns = [
    path('', views.index),
    path('chickens/create', views.create_chicken),
    path('chickens/<int:chicken_id>', views.show_chicken),
    path('chickens/<int:chicken_id>/destroy', views.delete_chicken),
    path('chickens/<int:chicken_id>/edit', views.edit_chicken),
    path('chickens/<int:chicken_id>/update',views.update_chicken),
]