from django.shortcuts import render, redirect
import bcrypt
from django.contrib import messages
from .models import *


def index(request):
    return render(request, "index.html",)

def create_user(request):
    if request.method == "POST":
        errors = User.objects.create_valdiator(request.POST)
        if len(errors) >0:
            for key, value in errors.items():
                messages.error(request, value)
                return redirect('/')
            else:
                password = request.POST['password']
                pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
                user = User.objects.create(name=request.POST['user_name'], email=request.POST['email'], password=pw_hash)
                request.session['user_id'] = user.id
                return redirect('/main_page')
    return redirect('/')

def main_page(request):
    if 'user_id' not in request.session:
        return redirect('/')
    context ={
        'current_user': User.objects.get(id=request.session['user_id']),
        'all_giraffes': Giraffe.objects.all()
    }
    return render(request, "main_page.html", context)

def login(request):
    if request.method =="POST":
        users_with_email = User.objects.filter(email=request.POST['email'])
        if users_with_email:
            user = users_with_email[0]
            if bcrypt.checkpw(request.POST['password'].encode(), user.password.encode()):
                request.session['user_id'] = user.id
                return redirect('/main_page')
            messages.error(request, "Email or password are not right")
    return redirect('/')

def logout(request):
    request.session.flush()
    return redirect('/')

def create_giraffe(request):
    if 'user_id' not in request.session:
        return redirect('/')
    if request.method == "POST":
        errors = Giraffe.objects.create_valdiator(request.POST)
        if len(errors) >0:
            for key, value in errors.items():
                messages.error(request, value)
                return redirect('/')
            else:
                giraffe = Giraffe.objects.create(name=request.POST['giraffe_name'], catchphrase=request.POST['catchphrase']
                , owner=User.objects.get(id=request.session['user_id']))
                return redirect('/main_page')
    return redirect('/main_page')

# Create your views here.
