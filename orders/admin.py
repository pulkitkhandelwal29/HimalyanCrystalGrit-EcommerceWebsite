from django.contrib import admin
from .models import Order, OrderProduct

class OrderProductInline(admin.TabularInline):
    model = OrderProduct
    readonly_fields = ('order', 'product', 'quantity')
    extra = 0

class OrderAdmin(admin.ModelAdmin):
    list_display = ['order_number', 'first_name', 'last_name', 'phone', 'email', 'created_at']
    search_fields = ['order_number', 'first_name', 'last_name', 'phone', 'email']
    list_per_page=20
    inlines = [OrderProductInline]


class OrderProductAdmin(admin.ModelAdmin):
    list_display = ['order', 'product','quantity']
    search_fields = ['order', 'product']
    list_per_page=20


# Register your models here.
admin.site.register(Order,OrderAdmin)
admin.site.register(OrderProduct,OrderProductAdmin)
