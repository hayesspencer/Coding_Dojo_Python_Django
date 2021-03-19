from django.shortcuts import render, redirect
LANGS = (
    'Python',
    'MERN',
    'Java',
)
LOCATIONS = (
    'San Jose',
    'Bellevue',
    'Oakland',
)

# Create your views here.
def index(request):
    context = {
        'locations': LOCATIONS,
        'languages': LANGS
    }
    return render(request, 'form.html', context)

def survey(request):
    if request.method == 'GET':
        return redirect('/')
    request.session['result'] = {
        'name': request.POST['name'],
        'location': request.POST['location'],
        'language': request.POST['language'],
        'comment': request.POST['comment']
    }
    return redirect('/result')

def result(request):
    context = {
        'result': request.session['result']
    }
    return render(request, 'result.html', context)


# Create your views here.
