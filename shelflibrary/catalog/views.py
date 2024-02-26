from django.shortcuts import render

from .models import Book, Author, BookInstance, Genre

from django.views import generic

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
    
    context = {
        'num_books': num_books,
        'num_instances':num_instances,
        'num_instances_available':num_instances_available,
        'num_authors':num_authors
    }
    
    # Render the HTML template index.html with the data in the context variable 
    return render(request, 'index.html',context=context)

# Class based views 
class BookListView(generic.ListView):
    model = Book
    
    context_object_name = 'book_list' # Your own name for the list as a template variable 
    queryset = Book.objects.filter(title__icontains = 'war')[:5] # Get 5 books containing the title war 
    template_name = 'books/book_list.html' # Specify your own template  name/location
    
    
class BookDetailView(generic.DetailView):
    model = Book
    