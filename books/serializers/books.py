from rest_framework import serializers
from authors.models import Author


class BookSerializer(serializers.ModelSerializer):


    class Meta:
        model = Author
        fields = ['id', 'title', 'author', 'published_date']
