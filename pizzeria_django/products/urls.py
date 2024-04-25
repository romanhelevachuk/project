from django.urls import path

from . import views

app_name = 'products'

urlpatterns = [
    path('list/', views.product_list_view, name='product_list'),
    path('detail/<int:pk>/', views.product_detail_view, name='product_detail'),
    path('add-to-basket/<int:pk>/', views.add_to_basket_view, name='add_to_basket'),
]
