from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def index(request):
    return HttpResponse("placeholder to later display list of blogs")

def new(request):
    return HttpResponse("Placedholder to display a new form to creat a new blog")

def create(request):
    return redirect('/')

def show(request, number):
    return HttpResponse(f"Placeholder to display blog number {number}.")

def edit(request, number):
    return HttpResponse(f"Placeholder to edit blog {number}.")

def destroy(request, number):
    return redirect('/')

def djangoOne(request):
    return render(request, "index.html")

    #  Create your views here