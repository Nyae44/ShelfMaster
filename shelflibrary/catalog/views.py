from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render

from .models import Book, Author, BookInstance, Genre

from django.views import generic
from django.shortcuts import get_object_or_404
from django.views.generic import DetailView

# Create your views here.

def index(request):
    """View function for home page of site"""
    # Generate the counts of some of the main objects 
    
    num_books = Book.objects.all().count
    num_instances = BookInstance.objects.all().count
    
    # Available books (status = 'a')
    num_instances_available = BookInstance.objects.filter(status = 'a').count()
    
    # The all is implied by default 
    num_authors = Author.objects.count()
    
    # Number of visits to this view, as counted in the session variable
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1
    
    context = {
        'num_books': num_books,
        'num_instances':num_instances,
        'num_instances_available':num_instances_available,
        'num_authors':num_authors
    }
    
    # Render the HTML template index.html with the data in the context variable 
    return render(request, 'index.html',context=context)
# Created a function based view because the class based view was not rendering the books list
def book_detail_view(request, primary_key):
    book = get_object_or_404(Book, pk= primary_key)
    return render(request,'catalog/book_detail.html', context={'book':book})
    

# Class based views 
class BookListView(generic.ListView):
    model = Book
    
    context_object_name = 'book_list' # Your own name for the list as a template variable 
    # queryset = Book.objects.filter(title__icontains = 'war')[:5] # Get 5 books containing the title war 
    queryset = Book.objects.all()
    template_name ='/home/nyae/django_projects/ShelfMaster/shelflibrary/catalog/templates/book_list.html' #Specify your template location

class BookDetailView(generic.DetailView):
    model = Book

    context_object_name = 'book'
    queryset = Book.objects.all()
    template_name = '/home/nyae/django_projects/ShelfMaster/shelflibrary/catalog/templates/book_detail.html'

  
class AuthorDetailView(generic.DetailView):
    model = Author
    context_object_name = 'author'
    template_name = 'home/nyae/django_projects/ShelfMaster/shelflibrary/catalog/templates/book_detail.html'

class AuthorsListView(generic.ListView):
    model = Author
    context_object_name = 'author_list'
    queryset = Author.objects.all()
    template_name = 'templates/author_list.html'
    

        