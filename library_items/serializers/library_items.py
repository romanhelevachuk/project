from rest_framework import serializers
from library_items.models import LibraryItem
from books.models import Book
from books.serializers import BookSerializer


class LibraryItemSerializer(serializers.ModelSerializer):
    book = BookSerializer()

    class Meta:
        model = LibraryItem
        fields = ['id', 'book', 'available']
