from django.db import models
from django.urls import reverse


class Product(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='goods/')

    def get_absolute_url(self):
        return reverse('products:product_detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.name
