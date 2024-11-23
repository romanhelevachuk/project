from django.urls import path
from . import views

urlpatterns = [
    path('', views.library_item_list, name='library_item_list'),
    path('<int:item_id>/', views.library_item_detail, name='library_item_detail'),
]
