from django.http import JsonResponse
from .models import Book

def book_list(request):
    books = Book.objects.all().values()
    return JsonResponse(list(books), safe=False)

def book_detail(request, book_id):
    book = Book.objects.get(id=book_id)
    return JsonResponse({"title": book.title, "author": book.author.name, "published_date": book.published_date})
