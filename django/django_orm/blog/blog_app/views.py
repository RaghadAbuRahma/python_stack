
from django.shortcuts import render, redirect 
from django.http import HttpResponseBadRequest
from django.contrib import messages
from .models import Blog



def update(request, id):
    errors = Blog.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/blog/edit/'+id)
    else:
        blog = Blog.objects.get(id = id)
        blog.name = request.POST['name']
        blog.desc = request.POST['desc']
        blog.save()
        messages.success(request, "Blog successfully updated")
        return redirect('')


def add_blog(request):
        name = request.POST['name']
        desc = request.POST['desc']

        Blog.objects.create(name=name, desc=desc)
        return render(request, 'index.html')
    
    




