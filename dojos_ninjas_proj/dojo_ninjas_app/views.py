from django.shortcuts import render, redirect
from .models import Dojo, Ninja


def index(request):
    context = {
        "dojos" : Dojo.objects.all()
    }
    return render(request, 'index.html', context)

def create_dojo(request):
    Dojo.objects.create(
        name=request.POST['name'],
        city=request.POST['city'],
        state=request.POST['state'],
    )
    return redirect('/')

def create_ninja(request):
    Ninja.objects.create(
        first_name=request.POST['first_name'],
        last_name=request.POST['last_name'],
        dojo_id=request.POST['dojo'],
    )
    return redirect('/')

# def delete(request):
#     objects = Db_test.objects.all()

#     if request.method == "POST":
#         # Fetch list of items to delete, by ID
#     items_to_delete = request.POST.getlist('delete_items')
#     # Delete those items all in one go
#     Db_test.objects.filter(pk__in=items_to_delete).delete()
# return render(request, "models_test/delete.html", {"values": objects})

# Create your views here.
