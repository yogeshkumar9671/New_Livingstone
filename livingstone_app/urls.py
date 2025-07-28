from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LogoutView

from django.conf import settings
from django.conf.urls.static import static

from .views import address_list_view, add_address_view


urlpatterns = [
    path('', views.index, name='index'),
    path('men/', views.men, name='men'),
    path('women/', views.women, name='women'),
    path('product/', views.product, name='product'),
    path('productdetails/', views.productdetails, name='productdetails'),
    path('addtocart/', views.addtocart, name='addtocart'),
    path('wishlist/', views.wishlist, name='wishlist'), 

    path('search/', views.search_products, name='search'),
    path('privacy_policy/', views.privacy_policy, name='privacy-policy'),

    path('refund_policy/', views.refund_policy, name='refund-policy'),
    path('tearms_policy/', views.tearms_policy, name='tearms-policy'),


    




    path('sign-in/', views.sign_in, name='sign_in'),
    path('create-account/', views.create_account, name='create_account'),
    path('logout/', views.custom_logout, name='logout'),
    path('verify-otp/', views.verify_otp, name='verify_otp'),
    path('reset-password/', auth_views.PasswordResetView.as_view(
        template_name='password_reset.html'), name='password_reset'),
    path('reset-password/done/', auth_views.PasswordResetDoneView.as_view(
        template_name='password_reset_done.html'), name='password_reset_done'),
    path('reset-password/confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name='password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset-password/complete/', auth_views.PasswordResetCompleteView.as_view(
        template_name='password_reset_complete.html'), name='password_reset_complete'),
    path('account/', views.account_dashboard, name='account'),
    path('dashboard/profile/', views.load_profile_section, name='load_profile_section'),
    path('track-order/', views.track_order, name='track_order'),
    path('profile/', views.profile_settings_view, name='profile_settings'),
    path('kashnaar/', views.kashnaar_view, name='kashnaar'),
    path('accessories/', views.accessories, name='accessories'),
    path('checkout-final/', views.checkout_final, name='checkout_final'),
    
    
    path('payment-done/', views.payment_done, name='payment_done'),
    path('payment-failed/', views.payment_failed, name='payment_failed'),


    path('my-orders/section/', views.load_order_history_section, name='load_order_history_section'),



    path('addresses/', views.address_list_view, name='address_list'),
    path('addresses/add/', views.add_address_view, name='add_address'),
    path('addresses/edit/<int:pk>/', views.edit_address_view, name='edit_address'),
    path('addresses/delete/<int:pk>/', views.delete_address_view, name='delete_address'),
    








 




    path('deliveryaddress/', views.Deliveryaddress, name="deliveryaddress"),
    path('products/<str:category>/<str:subcategory>/', views.product_list, name='product_list'),
    path('product/<int:product_id>/', views.product_details, name='productdetails'),

    
    path('add-to-cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),

    path('remove-cart-item/', views.remove_from_cart_backend, name='remove_cart_item'),

    path('cart/', views.cart, name='cart'),
    path('billing-address/', views.billing_address, name='billing_address'),
    path('checkout/', views.checkout, name='checkout'),
    path('paymentdone/', views.payment_done, name='paymentdone'),
    path('paymentfailed/', views.payment_failed, name='paymentfailed'),
    path('handlerequest/', views.handlerequest, name="handlerequest"),
    path('orders/', views.orders, name='orders'),
    path('tracker/', views.tracker, name="tracker"),

]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
