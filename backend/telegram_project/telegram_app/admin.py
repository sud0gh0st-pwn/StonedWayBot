from django.contrib import admin
from .models import MenuItem, Cart, CartItem, Order

admin.site.register(MenuItem)
admin.site.register(Cart)
admin.site.register(CartItem)
admin.site.register(Order)