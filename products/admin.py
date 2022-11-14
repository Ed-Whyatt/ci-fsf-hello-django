from django.contrib import admin
from .models import Product, Category
from django.views.decorators.csrf import csrf_exempt

# Register your models here.
admin.site.register(Product)
admin.site.register(Category)
