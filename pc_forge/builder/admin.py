from django.contrib import admin
from .models import Category, Product, Build, BuildItem

# This tells Django to create a graphical interface for these tables
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Build)
admin.site.register(BuildItem)