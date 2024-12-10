from django.db import models
from books.models import Book

class LibraryItem(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, default=1)
    available = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.book.title} - {'Available' if self.available else 'Not Available'}"
