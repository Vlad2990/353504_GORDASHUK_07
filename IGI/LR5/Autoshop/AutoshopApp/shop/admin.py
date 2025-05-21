from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(ProductCategory)
admin.site.register(News)
admin.site.register(Contact)
admin.site.register(Promocode)
admin.site.register(QandA)
admin.site.register(PickPoints)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'article', 'price')
    filter_horizontal = ('providers',)
    list_filter = ('providers', 'category')  

@admin.register(Provider)
class ProviderAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'phone_number', 'products_list')
    
    def products_list(self, obj):
        return ", ".join([p.name for p in obj.provider_product.all()[:3]]) + ("..." if obj.provider_product.count() > 3 else "")
    products_list.short_description = 'Products list'