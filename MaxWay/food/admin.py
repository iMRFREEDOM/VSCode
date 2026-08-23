from django.contrib import admin
from .models import Category, Product, Customer, Order, OrderProduct

# Modellarni admin panelga ro'yxatdan o'tkazish
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(OrderProduct)