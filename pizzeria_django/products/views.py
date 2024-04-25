from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from customers.models import BasketItem, Basket

from .models import Product


def index_view(request):
    """Використовується для відображення головної сторінки. Повертає шаблон головної сторінки."""
    context = {'title': 'Pizza Shop - Home'}
    return render(request, 'products/index.html', context)


def product_list_view(request):
    """Використовується для відображення списку продуктів. Повертає список продуктів."""
    products = Product.objects.all()
    context = {'title': 'Pizza Shop - Products', 'products': products}
    return render(request, 'products/product_list.html', context)


def product_detail_view(request, pk):
    """Використовується для відображення інформації про продукт. Повертає продукт."""
    product = get_object_or_404(Product, pk=pk)
    context = {'title': 'Pizza Shop - Product Detail', 'product': product}
    return render(request, 'products/product_detail.html', context)


@login_required
def add_to_basket_view(request, pk):
    """Використовується для додавання товару до кошика користувача. Перенаправляє на сторінку кошика."""
    if request.method == 'POST':
        product_id = request.POST.get('product_id')
        quantity = int(request.POST.get('quantity', 1))
        product = get_object_or_404(Product, pk=product_id)
        customer = request.user
        basket, created = Basket.objects.get_or_create(customer=customer)
        basket_item, item_created = BasketItem.objects.get_or_create(basket=basket, product=product)
        if not item_created:
            basket_item.quantity += quantity
            basket_item.save()
        else:
            basket_item.quantity = quantity
            basket_item.save()

        return redirect('customers:basket')
    else:
        return redirect('products:product_list')
