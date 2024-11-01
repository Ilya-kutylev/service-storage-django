# Регистрация моделей в админ-панели с настройкой отображения, поиска и фильтров
from django.contrib import admin
from .models import Product, ProductType, ProductPrice


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'quantity', 'barcode', 'updated_at', 'price_id', 'type_id')
    search_fields = ('name', 'barcode', 'type_id__name')
    list_filter = ('type_id', 'updated_at')
    list_editable = ('quantity',)
    ordering = ('-updated_at',)

    readonly_fields = ('updated_at',)

    fieldsets = (
        (None, {
            'fields': ('name', 'quantity', 'barcode', 'type_id')
        }),
        ('Price Information', {
            'fields': ('price_id',),
        }),
        ('Date Information', {
            'fields': ('updated_at',),
        }),
    )


@admin.register(ProductType)
class ProductTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)
    ordering = ('name',)


@admin.register(ProductPrice)
class ProductPriceAdmin(admin.ModelAdmin):
    list_display = ('currency', 'amount')
    search_fields = ('currency',)
    list_editable = ('amount',)
    ordering = ('currency',)
