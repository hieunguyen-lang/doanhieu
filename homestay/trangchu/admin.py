from django.contrib import admin
from.models import *
# Register your models here.

admin.site.register(Phong)
admin.site.register(Order_item)
admin.site.register(image_room)
admin.site.register(Order)
admin.site.register(customer_info)

class OrderItemInline(admin.StackedInline):
    model = Order_item
class OrderAdmin(admin.ModelAdmin):
    model = Order
    inlines = [OrderItemInline]
admin.site.unregister(Order)
admin.site.register(Order, OrderAdmin)