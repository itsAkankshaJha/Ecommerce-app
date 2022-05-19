from django.contrib import admin

# Register your models here.
from shopkaro.models import Category, SubCategory, Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(SubCategory)
class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ['sub_name']


@admin.register(Product)
class MyProductAdmin(admin.ModelAdmin):
    list_display = ['product_name', 'product_description', 'price', 'cat_id', 'subcat_id']
