from django.shortcuts import render, redirect
from .models import *
def index(request):
    context= {
    'all_books' : Book.objects.all()
    }
    return render(request, 'index.html', context)

def add_book(request):
    title = request.POST['title']
    description = request.POST['description']

    Book.objects.create(title=title, desc=description)

    return redirect('/')

def view_book(request, book_id):
    
    this_book = Book.objects.get(id=book_id)
    context = {'title': this_book.title, 'id': this_book.id, 'description' : this_book.desc, 'author': this_book.Authors.all()}


    return render(request, 'result.html', context)


def index2(request):
    context={
        'all_authors' : Author.objects.all()
        }
    return render(request, 'index2.html', context)


# def add_author(request):

def add_author(request):
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    notes = request.POST['notes']

    Author.objects.create(first_name=first_name, last_name=last_name, notes=notes)

    
    return redirect('/authors')



def view_author(request, id):
    this_author = Author.objects.get(id=id)
    context = {
        'first_name' : this_author.first_name, 'last_name': this_author.last_name,' id': this_author.id, 'book' :this_author.books.all()
        }
    
    return render(request, 'result2.html', context)
    

    
    
def select_author(request): 
    author_id = request.POST['author']
    author = Author.objects.get(id=author_id)

    Book.Author.add(author=author)
    redirect('/books')











    
