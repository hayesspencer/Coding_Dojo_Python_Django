from django.shortcuts import render, redirect

def index(request):
    return render(request, 'index.html')

def submission(request):
    if request.method == 'POST':
        context = {
            'name': request.POST['name'],
            'lang': request.POST['location'],
            'loc': request.POST['language'],
            'gen': request.POST['gender'],
            'cmmt': request.POST['comment']
        }
        return render(request, 'results.html', context)
    return render(request, 'results.html')

# Create your views here.
