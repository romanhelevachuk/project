from django.http import JsonResponse
from .models import LibraryItem

def library_item_list(request):
    items = LibraryItem.objects.all().values()
    return JsonResponse(list(items), safe=False)

def library_item_detail(request, item_id):
    item = LibraryItem.objects.get(id=item_id)
    return JsonResponse({"book": item.book.title, "available": item.available})
