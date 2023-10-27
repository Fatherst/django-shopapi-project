from django.contrib import admin
from .models import Product, Category, ProductImage, Tag
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'price',
                    'date','freeDelivery','rating','reviews',
                    'category','tags')

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = "title",

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = "name",

@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    list_display = "src","alt"