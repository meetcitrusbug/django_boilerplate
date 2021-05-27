from django.contrib import admin
from order.models import Order, Address, OrderProduct, UserCard

# Register your models here.

class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'order_id', 'total_amount', 'status', 'created_at']
    
class AddressAdmin(admin.ModelAdmin):
    list_display = ['id', 'street', 'city', 'state', 'country', 'type']

class OrderProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'order', 'product', 'quantity']

class CardAdmin(admin.ModelAdmin):
    list_display = ['user', 'card_number','created_at']

admin.site.register(Order,  OrderAdmin)
admin.site.register(Address,  AddressAdmin)
admin.site.register(OrderProduct,  OrderProductAdmin)
admin.site.register(UserCard,  CardAdmin)