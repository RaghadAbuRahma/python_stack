from django.shortcuts import render, redirect, HttpResponse
from .models import *
from django.contrib import messages

def update(request, id):
    errors = Show.objects.basic_validator(request.POST)
    

    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        show = Show.objects.get(id = id)
        return redirect(f'/show/{show.id}/edit')
    else:
        
        show.title = request.POST['title']
        show.Network = request.POST['network']
        Show.release_date = request.POST['release_date']
        show.save()
        messages.success(request, "Show successfully updated")
        return redirect('/shows')
    
def index(request):
    shows = Show.objects.all()
    context= { 'shows' : shows }
    return render(request, 'index.html', context)


def new_show(request): 
    return render(request, 'new_show.html')


def create_show(request):
    errors = Show.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('shows/new')
    else:
        title = request.POST['title']
        Network = request.POST['network']
        release_date = request.POST['release_date']
        create = Show.objects.create(title=title, Network=Network, release_date=release_date)
        messages.success(request, "Show successfully created")
        return redirect(f'/show/{create.id}')

def view_show(request, id): 
    this_show = Show.objects.get(id=id)
    context = { 'ID': this_show.id, 'title' : this_show.title, 'Network': this_show.Network, 'released_date': this_show.release_date
    }

    return render(request, 'view_show.html', context)

def edit(request, id): 
    edit = Show.objects.get(id=id)
    context = {'id': edit.id,  'title': edit.title, 'Network': edit.Network, 'release_date': edit.release_date}

    return render(request, 'edit.html', context) 


    
def delete(request, id): 
    to_delete = Show.objects.get(id=id)
    to_delete.delete()
    return redirect ('/shows')

def back(request):
    return redirect('/shows')

# def update(request, id): 
#     Title = request.POST['title']
#     Network = request.POST['Network']
#     release_date = request.POST['release_date']

#     to_update = Show.objects.get(id=id)
#     to_update.title= Title
#     to_update.Network= Network
#     to_update.release_date = release_date
#     to_update.save()
    

#     return redirect ('/shows')






    





