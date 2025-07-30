from django.contrib import admin
from .models import Profile, Product, CartItem, Order_Tracker, Placed_Order, Address, Color, Size

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'first_name', 'last_name', 'gender', 'mobile', 'phone')



# for product listing admin panelfrom django.contrib import admin

from django.contrib import admin
from .models import Product


@admin.register(Address)
class AddressModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'full_name', 'locality', 'city', 'pincode', 'state']


from django.urls import reverse
@admin.register(CartItem)
class CartModelAdmin(admin.ModelAdmin):
    list_display = ['user', 'order_id', 'product_detail', 'quantity']

    def product_detail(self, obj):
        link = reverse("admin:livingstone_app_product_change", args=[obj.product.pk])
        return format_html('<a href="{}">{}</a>', link, obj.product.title)




@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'subcategory', 'price', 'get_colors', 'get_sizes')
    list_filter = ('category', 'subcategory')
    search_fields = ('title', 'description')
    filter_horizontal = ('color', 'size')  # Matches field names in your Product model

    def get_colors(self, obj):
        return ", ".join([color.name for color in obj.color.all()])
    get_colors.short_description = 'Colors'

    def get_sizes(self, obj):
        return ", ".join([size.name for size in obj.size.all()])
    get_sizes.short_description = 'Sizes'

@admin.register(Color)
class ColorAdmin(admin.ModelAdmin):
    list_display = ['name', 'hex_code']

@admin.register(Size)
class SizeAdmin(admin.ModelAdmin):
    list_display = ['name']




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
        

