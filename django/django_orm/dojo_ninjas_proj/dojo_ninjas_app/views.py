from django.shortcuts import render, redirect
from .models import *

def index(request): 
    context= {"Dojos": Dojo.objects.all()}
    return render(request, "index.html", context)

def addDojo(request): 
    name = request.POST['name']
    city = request.POST['city']
    state = request.POST['state']

    Dojo.objects.create(name=name, city=city, state=state)
    return redirect('/')


def addNinja(request):
    fisrt_name= request.POST['first_name']
    last_name= request.POST['last_name']
    dojo_id = request.POST['dojo']
    # print(dojo_id)
    dojo = Dojo.objects.get(id=dojo_id)
    
    Ninja.objects.create(first_name=fisrt_name, last_name=last_name, dojo=dojo)
    return redirect('/')
