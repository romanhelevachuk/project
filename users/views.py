from django.http import JsonResponse
from .models import User

def user_list(request):
    users = User.objects.all().values()
    return JsonResponse(list(users), safe=False)

def user_detail(request, user_id):
    user = User.objects.get(id=user_id)
    return JsonResponse({"username": user.username, "email": user.email})
