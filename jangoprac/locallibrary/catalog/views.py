from django.shortcuts import render
from catalog.models import Genre, Book, BookInstance, Author
from django.views import generic
# Create your views here.

def index(request):
    """View function for homepage of site"""

    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()

    # Available Books
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()

    num_authors = Author.objects.count()

    context = {
        'num_books': num_books,
        'num_instances' : num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors
    }

    return render(request, 'index.html', context=context)

def books(request):
    """View function for books"""

    books = Book.objects.all()

    context = {
        'books': books
    }

    return render(request, 'book_list.html', context=context)

def book_detail(request, pk):
    """View function for book detail"""

    book = Book.objects.get(id=pk)

    context = {
        'book': book
    }

    return render(request, 'book_detail.html', context=context)

def authors(request):
    """View function for authors"""

    authors = Author.objects.all()

    context = {
        'authors': authors
    }

    return render(request, 'author_list.html', context=context)

def author_detail(request, pk):
    """View function for author details"""

    author = Author.objects.get(id=pk)

    context = {
        'author': author
    }

    return render(request, 'author_detail.html' , context)
