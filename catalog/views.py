from django.shortcuts import render
from .models import Book, Author, Genre, BookInstance, Genre
from .serializer import BookSerializer, AuthorSerializer, GenreSerializer
from rest_framework import viewsets, permissions
from django.views import generic
# creating collection of objects from given Class and deserializing
class BookViewSet(viewsets.ModelViewSet):

    queryset = Book.objects.all()
    serializer_class = BookSerializer

class AuthorViewSet(viewsets.ModelViewSet):

    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class GenreViewSet(viewsets.ModelViewSet):

    queryset = Genre.objects.all()
    serializer_class = GenreSerializer

def index(request):

    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()
    num_instances_available = BookInstance.objects.all().filter(status__exact='a').count()
    num_authors = Author.objects.count()
    num_genres = Genre.objects.count()


    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
        'num_genres': num_genres,
    }
    file_object = open('sample.txt', 'a')
    file_object.write(str(request))
    file_object.close()
    return render(request, 'index.html', context=context)

class BookListView(generic.ListView):
    model = Book

class BookDetailView(generic.ListView):
    model = Book