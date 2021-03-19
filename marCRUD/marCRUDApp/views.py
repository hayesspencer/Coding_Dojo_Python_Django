from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages

def index(request):
    context = {
        "all_chickens" : Chicken.objects.all()
    }
    return render(request, "index.html", context)

def create_chicken(request):
    if request.method == "POST":
        errors = Chicken.objects.create_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/')
        else:
            chicken = Chicken.objects.create(name=request.POST['chicken_name'], color= request.POST['color'])
    return redirect('/')

def show_chicken(request, chicken_id):
    context = {
        'one_chicken': Chicken.objects.get(id=chicken_id)
    }
    return render(request, "one_chicken.html", context)

def delete_chicken(request, chicken_id):
    if request.method == "POST":
        chicken_to_delete = Chicken.objects.get(id=chicken_id)
        chicken_to_delete.delete()
    return redirect('/')

def edit_chicken(request, chicken_id):
    context = {
        'one_chicken': Chicken.objects.get(id=chicken_id)
    }
    return render(request, "edit_chicken.html", context)

def update_chicken(request, chicken_id):
    if request.method == "POST":
        errors = Chicken.objects.edit_validator(request.POST, chicken_id)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect(f'/chickens/{chicken_id}/edit')
        else:
            chicken = Chicken.objects.get(id=chicken_id)
            chicken.name = request.POST['chicken_name']
            chicken.color = request.POST['color']
            chicken.save()
            return redirect(f'/chickens/{chicken_id}')
    return redirect('/')





# Create your views here.
