from django.urls import path

from . import views

app_name = 'customers'

urlpatterns = [
    path('basket/', views.basket_view, name='basket'),
    path('remove-from-basket/<int:pk>/', views.basket_item_remove_view, name='remove-item'),
    path('create-order/', views.create_order_view, name='create_order'),
    path('order/<int:pk>/', views.order_detail_view, name='order-detail'),
    path('generate-pdf/<int:order_id>/', views.generate_pdf, name='generate_pdf'),

]
