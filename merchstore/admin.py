from django.contrib import admin
from .models import ProductType, Product, Transaction


class ProductInline(admin.TabularInline):
    model = Product


class ProductTypeAdmin(admin.ModelAdmin):
    model = ProductType
    inlines = [ProductInline,]


class ProductAdmin(admin.ModelAdmin):
    model = Product


class TransactionAdmin (admin.ModelAdmin):
    model = Transaction


admin.site.register(ProductType, ProductTypeAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Transaction, TransactionAdmin)
