from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages

def index(request):
    context = {
        "all_books" : Book.objects.all()
    }
    return render(request, "index.html", context)

# Create your views here.
