from django.contrib import admin

from . import models


@admin.register(models.Customer)
class CustomerAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Basket)
class BasketAdmin(admin.ModelAdmin):
    pass


@admin.register(models.BasketItem)
class BasketItemAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Order)
class OrderAdmin(admin.ModelAdmin):
    pass
