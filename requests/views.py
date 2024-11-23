from django.http import JsonResponse
from .models import Request

def request_list(request):
    requests = Request.objects.all().values()
    return JsonResponse(list(requests), safe=False)

def request_detail(request, request_id):
    request = Request.objects.get(id=request_id)
    return JsonResponse({
        "user": request.user.username,
        "library_item": request.library_item.book.title,
        "status": request.status
    })
