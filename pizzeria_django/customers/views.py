from django.http import FileResponse
from reportlab.pdfgen import canvas
from django.contrib.auth.decorators import login_required
from customers.models import Basket
from django.shortcuts import redirect, get_object_or_404, render
from .models import BasketItem, Order


@login_required
def basket_view(request):
    """Використовується для відображення кошика користувача. Повертає список товарів у кошику."""
    basket = get_object_or_404(Basket, customer=request.user)
    basket_items = basket.items.all()
    return render(request, 'customers/basket.html', {'basket_items': basket_items})


@login_required
def basket_item_remove_view(request, pk):
    """Використовується для видалення товару з кошика користувача."""
    basket_item = get_object_or_404(BasketItem, pk=pk, basket__customer=request.user)
    if request.method == 'POST':
        quantity_to_remove = int(request.POST.get('quantity', 1))
        if quantity_to_remove > basket_item.quantity:
            return redirect('basket:remove-item', pk=basket_item.pk)
        basket_item.quantity -= quantity_to_remove
        if basket_item.quantity <= 0:
            basket_item.delete()
        else:
            basket_item.save()
        return redirect('customers:basket')
    return redirect('customers:basket')


@login_required
def create_order_view(request):
    """Використовується для створення замовлення користувача. Перенаправляє на сторінку інформації про замовлення."""
    if request.method == 'POST':
        customer = request.user
        basket = Basket.objects.get(customer=customer)
        total_price = sum(item.product.price * item.quantity for item in basket.items.all())

        order = Order.objects.create(customer=customer, total_price=total_price)

        basket.active = False
        basket.save()

        return redirect('customers:order-detail', pk=order.pk)
    else:
        return render(request, 'customers/basket.html')


@login_required
def generate_pdf(request, order_id):
    """Використовується для генерації PDF-файлу з інформацією про замовлення. Повертає PDF-файл."""
    response = FileResponse(
        generate_pdf_file(
            order_id=order_id),
        as_attachment=True,
        filename='book_catalog.pdf'
    )
    return response


def generate_pdf_file(order_id):
    from io import BytesIO

    buffer = BytesIO()
    p = canvas.Canvas(buffer)

    order = Order.objects.get(pk=order_id)

    # Create a PDF document
    p.drawString(100, 750, "Order Details")
    p.drawString(100, 730, f"Order ID: {order.id}")
    p.drawString(100, 710, f"Customer: {order.customer.username}")
    p.drawString(100, 690, f"Total Price: {order.total_price}")
    p.drawString(100, 670, f"Order Address: {order.address}")
    p.drawString(100, 650, f"Created At: {order.created_at}")
    p.drawString(100, 630, f"Updated At: {order.updated_at}")

    p.showPage()
    p.save()

    buffer.seek(0)
    return buffer


def order_detail_view(request, pk):
    """Використовується для відображення інформації про замовлення. Повертає інформацію про замовлення."""
    order = get_object_or_404(Order, pk=pk, customer=request.user)
    return render(request, 'customers/order_detail.html', {'order': order})
