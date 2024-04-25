from django.db import models
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver


class CustomerManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(is_customer=True)


class Customer(get_user_model()):
    objects = CustomerManager()

    class Meta:
        proxy = True

    def save(self, *args, **kwargs):
        self.is_student = True
        super().save(*args, **kwargs)


@receiver(post_save, sender=get_user_model())
def create_basket_for_new_customer(sender, instance, created, **kwargs):
    if created and instance.is_customer:
        Basket.objects.create(customer=instance)


class Basket(models.Model):
    customer = models.OneToOneField(Customer, on_delete=models.CASCADE)
    active = models.BooleanField(default=True)


class BasketItem(models.Model):
    basket = models.ForeignKey(Basket, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey('products.Product', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f'Basket ID: {self.id} | Owner: {self.basket.customer.username} |{self.product.name} - Quantity: {self.quantity}'


class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    address = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Order ID: {self.id} | Owner: {self.customer.username} | Total Price: {self.total_price}'
