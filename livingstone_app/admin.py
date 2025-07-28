from django.contrib import admin
from .models import Profile, Product, CartItem, Order_Tracker, Placed_Order, Address, Order, OrderItem

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'first_name', 'last_name', 'gender', 'mobile', 'phone')



# for product listing admin panelfrom django.contrib import admin

from django.contrib import admin
from .models import Product




from django.urls import reverse
@admin.register(CartItem)
class CartModelAdmin(admin.ModelAdmin):
    list_display = ['user', 'order_id', 'product_detail', 'quantity']

    def product_detail(self, obj):
        link = reverse("admin:livingstone_app_product_change", args=[obj.product.pk])
        return format_html('<a href="{}">{}</a>', link, obj.product.title)




@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'subcategory', 'price', 'color', 'size')
    list_filter = ('category', 'subcategory', 'color', 'size')
    search_fields = ('title', 'description')




from django.utils.html import format_html
from django.urls import reverse
@admin.register(Placed_Order)
class OrderPlacedModelAdmin(admin.ModelAdmin):
    list_display = ['user', 'order_id', 'customer_info', 'product_info', 'quantity', 'price', 'payment_status', 'status']
    
    def customer_info(self, obj):
        link = reverse("admin:livingstone_app_address_change", args=[obj.address.pk])
        return format_html("<a href='{}'>{}</a>", link, obj.address.full_name)

        
    def product_info(self, obj):
        link = reverse("admin:livingstone_app_product_change", args=[obj.product.pk])
        return format_html('<a href="{}">{}</a>', link, obj.product.title)




@admin.register(Order_Tracker)
class OrderUpdateModelAdmin(admin.ModelAdmin):
    list_display = ['tracking_id', 'order_info', 'update_desc', 'timestamp']
    
    def order_info(self, obj):
        if obj.orderInfo:
            link = reverse("admin:{}_{}_change".format(obj.orderInfo._meta.app_label, obj.orderInfo._meta.model_name), args=[obj.orderInfo.pk])
            return format_html("<a href='{}'>{}</a>", link, obj.orderInfo.product_id_number)
        else:
            return "No order information"
        




# for order history produuct save

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('order_id', 'user', 'created_at', 'paid_amount')

@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('order', 'product', 'quantity', 'delivery_status')


# @admin.register(CartItem)
# class CartItemAdmin(admin.ModelAdmin):
#     list_display = ('user', 'product', 'quantity', 'added_at')

