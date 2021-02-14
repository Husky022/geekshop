from django.contrib import admin

# Register your models here.

from mainapp.models import ProductCategory, Product

admin.site.register(ProductCategory)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'quantity')
    fields = ('name', 'image', 'description', 'short_description', 'price', 'quantity', 'category')
    # readonly_fields = ('short_description',)
    ordering = ('name',)
    search_fields = ('name','category__name',)