from .models import Book, Author, Genre
from rest_framework import serializers

#serializing models and defining avaiable fields

class AuthorSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Author
        fields = ['id', 'first_name', 'last_name']

class GenreSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Genre
        fields = ['id', 'name']

class BookSerializer(serializers.HyperlinkedModelSerializer):
    #author should show only name and surname, not attributes of Author class
    author = serializers.CharField()
    # display_genre attribute changes name to 'genre' for better readability
    genre = serializers.CharField(source='display_genre')
    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'genre']




