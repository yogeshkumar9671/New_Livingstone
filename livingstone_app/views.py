from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from .models import UserProfile, Address
import random
from django.contrib.auth.decorators import login_required
from .forms import ProfileForm
from django.views.decorators.csrf import csrf_exempt


from .models import Profile, Address, Placed_Order, Order_Tracker, Order
from .forms import AddressForm




def index(request):
    return render(request, 'index.html')


def men(request):
    return render(request, 'men.html')

# class ProfileView(View):
#     def get(self, request):
#         TotalCartItems=0
#         if request.user.is_authenticated:
#             TotalCartItems = len(Cart_Item.objects.filter(user=request.user))
#             forms = CustomerAddressForm()
#             context = {
#                 'forms':forms,
#                 "TotalCartItems":TotalCartItems,
#             }
#             return render(request, 'app/profile.html',context)
#         else: 
#             return redirect("/login")

#     def post(self, request):
#         if request.method == "POST":
#             forms = CustomerAddressForm(request.POST)
            
#             if forms.is_valid():
#                 current_user = request.user
#                 full_name = forms.cleaned_data['full_name']
#                 locality = forms.cleaned_data['locality']
#                 mobile=forms.cleaned_data['mobile_number']
#                 email=forms.cleaned_data['email']
#                 house_no=forms.cleaned_data['house_no']
#                 area=forms.cleaned_data['area']
#                 landmark=forms.cleaned_data['landmark']
#                 state = forms.cleaned_data['state']
#                 city = forms.cleaned_data['city']
#                 pincode = forms.cleaned_data['pincode']
#                 home = forms.cleaned_data['home']
#                 office = forms.cleaned_data['office']
                
#                 address_type = request.POST.get("addressType")
                
#                 if address_type == "home":
#                     home_address = True
#                 else:
#                     home_address = False
                    
#                 if address_type == "office":
#                     office_address = True
#                 else:
#                     office_address = False
                
#                 address = Address(user=current_user, full_name=full_name, locality=locality, mobile_number=mobile, email=email, house_no=house_no, area=area, landmark=landmark, state=state, city=city, pincode=pincode, home=home_address, office=office_address)
#                 address.save()
#                 messages.success(request, "Congratulations !! Profile Updated Successfully.")
        
#         forms = CustomerAddressForm()
#         context = {
#             'forms':forms
#         }
#         return render(request, 'app/profile.html',context)
    
    


# class ProductView(View):
#     def get(self, request):
#         TotalCartItems=0
#         if request.user.is_authenticated:
#             TotalCartItems = len(Cart_Item.objects.filter(user=request.user))

#         featured_product = Product.objects.filter(category='FEATURED')[:5]

#         context={
#         "featured":featured_product,
#         "TotalCartItems":TotalCartItems,
#         }
#         return render(request, 'app/home.html',context)
    
    



    


def women(request):
    return render(request, 'women.html')

def product(request):
    return render(request, 'product.html')

def productdetails(request):
    return render(request, 'productdetails.html')

def addtocart(request):
    return render(request, 'addtocart.html')

def cart(request):
    return render(request, 'cart.html')

def wishlist(request):
    return render(request, 'wishlist.html')




def search_products(request):
    query = request.GET.get('q', '')
    sort = request.GET.get('sort', 'relevance')
    selected_price = request.GET.get('price')
    selected_subcategory = request.GET.get('subcategory')

    products = Product.objects.all()

    if query:
        products = products.filter(
            Q(title__icontains=query) |
            Q(category__icontains=query) |
            Q(subcategory__icontains=query)
        )

    if selected_subcategory:
        products = products.filter(subcategory=selected_subcategory)

    if selected_price:
        try:
            min_price, max_price = map(int, selected_price.split('-'))
            products = products.filter(price__gte=min_price, price__lte=max_price)
        except ValueError:
            pass

    
    if sort == 'low_to_high':
        products = products.order_by('price')
    elif sort == 'high_to_low':
        products = products.order_by('-price')
    elif sort == 'newest':
        products = products.order_by('-id')
    else:  
        products = products.order_by('title')

    return render(request, 'search_list.html', {
        'products': products,
        'query': query,
        'sort': sort,
        'selected_price': selected_price,
        'selected_subcategory': selected_subcategory
    })



def track_order(request):
    return render(request, 'track_order.html')

def accessories(request):
    return render(request, 'accessories.html')




def kashnaar_view(request):
    return render(request, 'kashnaar.html')


# def guest_checkout(request):
#     return render(request, 'guest_checkout.html')


def privacy_policy(request):
    return render(request, 'privacy Policy.html')

def refund_policy(request):
    return render(request, 'refund policy.html') 
def tearms_policy(request):
    return render(request, 'tearms policy.html')   




#LOGIN VIEW
def sign_in(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, username=email, password=password)
        if user is not None:
            if user.userprofile.is_verified:
                login(request, user)
                return redirect('index')  
            else:
                messages.error(request, 'Please verify your account first.')
        else:
            messages.error(request, 'Invalid email or password.')
    return render(request, 'signIn.html')


# CREATE ACCOUNT VIEW
def create_account(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        confirm_email = request.POST.get('confirm_email')
        password = request.POST.get('password')
        re_password = request.POST.get('re_password')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')

        if email != confirm_email:
            messages.error(request, "Emails do not match.")
            return render(request, 'login.html')

        if password != re_password:
            messages.error(request, "Passwords do not match.")
            return render(request, 'login.html')

        if User.objects.filter(username=email).exists():
            messages.error(request, "Email already registered.")
            return render(request, 'login.html')

        user = User.objects.create_user(username=email, email=email, password=password,
                                        first_name=first_name, last_name=last_name)
        user.is_active = False
        user.save()

        Profile.objects.get_or_create(user=user)

        otp = str(random.randint(100000, 999999))
        profile = user.userprofile
        profile.otp = otp
        profile.save()

        send_mail(
            'Your OTP Verification Code',
            f'Hello {first_name},\n\nYour OTP is: {otp}\nPlease verify to activate your account.',
            settings.EMAIL_HOST_USER,
            [email],
            fail_silently=False,
        )

        request.session['email'] = email
        return redirect('verify_otp')

    return render(request, 'login.html')


#  OTP VALIDATION VIEW
def verify_otp(request):
    email = request.session.get('email')
    if not email:
        messages.error(request, "Session expired. Please register again.")
        return redirect('create_account')

    user = User.objects.get(username=email)
    profile = user.userprofile

    if request.method == 'POST':
        otp = ''.join([
            request.POST.get('otp1', ''),
            request.POST.get('otp2', ''),
            request.POST.get('otp3', ''),
            request.POST.get('otp4', ''),
            request.POST.get('otp5', ''),
            request.POST.get('otp6', ''),
        ])

        if profile.otp == otp:
            profile.is_verified = True
            profile.otp = ''
            profile.save()
            user.is_active = True
            user.save()
            messages.success(request, "Account verified successfully! Please log in.")
            return redirect('sign_in')
        else:
            messages.error(request, "Incorrect OTP")

    return render(request, 'otpvalidation.html')


# Logout View
def custom_logout(request):
    logout(request)
    return redirect('index')


# user account
def account_dashboard(request):
    return render(request, 'dashboard.html')


def load_profile_section(request):
    return render(request, 'profile_settings.html')






# for save user profile details


@login_required
def profile_settings_view(request):
    user = request.user

    if request.method == 'POST':
        user.email = request.POST.get('email')
        user.first_name = request.POST.get('first_name')
        user.last_name = request.POST.get('last_name')
        user.save()

        profile, _ = Profile.objects.get_or_create(user=user)
        profile.gender = request.POST.get('gender')
        profile.mobile = request.POST.get('mobile_number')
        profile.phone = request.POST.get('phone_number')
        profile.first_name = request.POST.get('first_name')
        profile.last_name = request.POST.get('last_name')
        profile.save()

        return redirect('profile_settings')
    
    return render(request, 'profile_settings.html')



from django.shortcuts import render, get_object_or_404
from .models import Product

# Product list view with category and subcategory filtering
def product_list(request, category=None, subcategory=None):
    products = Product.objects.all()
    
    if category:
        products = products.filter(category=category)

    # Only filter by subcategory if it's not all
    if subcategory and subcategory.lower() != 'all':
        products = products.filter(subcategory=subcategory)

    context = {
        'products': products,
        'category': category.capitalize() if category else '',
        'subcategory': '' if subcategory and subcategory.lower() == 'all' else subcategory.replace('_', ' ').capitalize() if subcategory else '',
    }
    return render(request, 'product.html', context)










from django.db.models import Q
# Product details view with breadcrumb context
def product_details(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    item_already_in_cart = False
    if request.user.is_authenticated:
        item_already_in_cart = CartItem.objects.filter(Q(product=product.id) & Q(user=request.user)).exists() 

    TotalCartItems=0
    if request.user.is_authenticated:
        TotalCartItems = len(CartItem.objects.filter(user=request.user))

    context = {
        'product': product,
        'category': product.get_category_display(),
        'subcategory': product.get_subcategory_display(),
        "item_already_in_cart":item_already_in_cart,
        "TotalCartItems":TotalCartItems,
    }
    return render(request, 'productdetails.html', context)















# view for inventory management


from .models import Product, CartItem

def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    quantity_requested = int(request.POST.get('quantity'))
    item_already_in_cart = CartItem.objects.filter(Q(product=product_id) & Q(user=request.user)).exists() 

    if product_id:
        if item_already_in_cart and product.quantity >= quantity_requested:
            cart_product = CartItem.objects.get(product=product, user=request.user)
            cart_product.quantity = quantity_requested
            cart_product.availability = False
            cart_product.save()
            return redirect('/cart')
            
        elif not item_already_in_cart and product.quantity >= quantity_requested:
            CartItem(product=product, quantity=quantity_requested, availability=False,  user=request.user).save()
            messages.success(request, f"{product.title} added to cart.")

        else:
            messages.error(request, "Not enough stock available.")
            return redirect('productdetails', product_id=product.id)    
    else:
        messages.error(request, "Not enough stock available.")
    return redirect('productdetails', product_id=product.id)





from .models import CartItem

@csrf_exempt
def remove_from_cart_backend(request):
    if request.method == 'POST':
        item_id = request.POST.get('item_id')
        try:
            item = CartItem.objects.get(id=item_id)
            item.delete()
            return JsonResponse({'success': True})
        except CartItem.DoesNotExist:
            return JsonResponse({'success': False, 'error': 'Item not found'})
    return JsonResponse({'success': False, 'error': 'Invalid request'})





from livingstone_app.forms import CustomerAddressForm
@login_required(login_url="/login")
def billing_address(request):
    TotalCartItems=0
    if request.user.is_authenticated:
        TotalCartItems = len(CartItem.objects.filter(user=request.user))

    user=request.user
    add=Address.objects.filter(user=user)
    # cart=Cart_Item.objects.filter(user=user)
    cart=CartItem.objects.filter(user=user, availability=True)
    
    if not cart:
        messages.error(request, "Product is out of stock")
        return redirect('/addtocart')

    if request.method == "POST":
        forms = CustomerAddressForm(request.POST)
        if forms.is_valid():
            current_user = request.user
            full_name = forms.cleaned_data['full_name']
            locality = forms.cleaned_data['locality']
            mobile=forms.cleaned_data['mobile_number']
            email=forms.cleaned_data['email']
            house_no=forms.cleaned_data['house_no']
            area=forms.cleaned_data['area']
            landmark=forms.cleaned_data['landmark']
            state = forms.cleaned_data['state']
            city = forms.cleaned_data['city']
            pincode = forms.cleaned_data['pincode']
            home = forms.cleaned_data['home']
            office = forms.cleaned_data['office']
            address_type = request.POST.get("addressType")
            
            if address_type == "home":
                home_address = True
            else:
                home_address = False
                
            if address_type == "office":
                office_address = True
            else:
                office_address = False
            
            address = Address(user=current_user, full_name=full_name, locality=locality, mobile_number=mobile, email=email, house_no=house_no, area=area, landmark=landmark, state=state, city=city, pincode=pincode, home=home_address, office=office_address)
            address.save()
            messages.success(request, "Congratulations !! Profile Updated Successfully.")
        
    forms = CustomerAddressForm()
    context = {
        'forms':forms,
        "add":add,
        "TotalCartItems":TotalCartItems
    }
    return render(request, 'deliveryaddress.html',context)















# # ============= PayUmoney integration ==============
# # ============= PayUmoney integration ==============

from django.contrib.sites.shortcuts import get_current_site
from django.conf import settings
from paywix.payu import Payu
import hashlib
from random import randint
@login_required(login_url="/login")


def checkout(request):
    
    TotalCartItems=0
    if request.user.is_authenticated:
        TotalCartItems = len(CartItem.objects.filter(user=request.user))

    user=request.user
    custadd=request.GET.get('custid')
    add=Address.objects.filter(id=custadd)
    cart_items=CartItem.objects.filter(user=user, availability=True)

    if not add:
        messages.error(request, "Please Select At Least One Shipping Address")
        return redirect('/billing-address')

    amount = 0
    order=0
    totalamount = 0
    selling_price = 0
    cart_product = [p for p in CartItem.objects.all() if p.user == request.user and p.availability==True]
    if cart_product:
        for p in cart_product:
            tempamount = (p.quantity*p.product.price)
            amount += tempamount
            
            totalamount = amount
            p.address=custadd
            
            product_id = p.datetime.strftime('PDOLIFT%Y%m%dODR') + str(p.id)
            p.product_id_number=product_id
            
            p_title = p.product.title
            
        order_id = p.datetime.strftime('PAY2LIFT%Y%m%dODR') + str(p.id)
        
        for p in cart_product:
            p.order_id=order_id
            
        
        if product_id is not None:   

            productinfo=[]
            for p in cart_product:
                productinfo.append(p.product.title)

            buyer_details=Address.objects.get(id=custadd)
            
            payu_config = settings.PAYU_CONFIG
            merchant_key = payu_config.get('merchant_key')
            merchant_salt = payu_config.get('merchant_salt')
            mode = payu_config.get('mode')
            
            # generate a random transaction Id.
            hash_object = hashlib.sha256(str(randint(0,9999)).encode("utf-8"))
            txnid = hash_object.hexdigest().lower()[0:16]
            
            
            # create hash string using all the fields
            hash_string = merchant_key+"|"+txnid+"|"+str(float(totalamount))+"|"+p_title+"|"
            hash_string += buyer_details.full_name+"|"+buyer_details.email+"|"
            hash_string += "||||||||||"+merchant_salt

            
            # # generate the hash
            generated_hash = hashlib.sha512(hash_string.encode('utf-8')).hexdigest().lower()

            
            payu_config = settings.PAYU_CONFIG
            merchant_key = payu_config.get('merchant_key')
            merchant_salt = payu_config.get('merchant_salt')
            mode = payu_config.get('mode')
            
            txnid = txnid
            hash_string = hash_string
            hash_ = generated_hash
            surl = 'http://'+ str(get_current_site(request))+"/handlerequest/"
            furl = 'http://'+ str(get_current_site(request))+"/paymentfailed/"
            # surl = 'http://'+ str(get_current_site(request))+"/handlerequest/"
            # furl = 'http://'+ str(get_current_site(request))+"/paymentfailed/"
            
            payu = Payu(merchant_key, merchant_salt, mode)         
            
            data = {
                "amount": totalamount,
                "firstname": buyer_details.full_name,
                "email": buyer_details.email,
                "productinfo": productinfo,
                "phone": buyer_details.mobile_number,
                "surl": surl,
                "furl": furl,
                "service_provider" : "livingstoneinstitute",
                "txnid" : txnid,
                "hash" : hash_,
                "hash_string" : hash_string,
            }
            print("====", data)
            data.update({"txnid": txnid})

            Payu_data = payu.transaction(**data)

            for p in cart_product:
                p.transaction_id = txnid
                p.save()
            
        else:
            messages.error(request, "Order Id is Missing")
            return redirect('/deliveryaddress')

        callback_url = 'https://'+ str(get_current_site(request))+"/handlerequest/"
    context={
        "add":add,
        "totalamount":totalamount,
        "cart_items":cart_items,
        "callback_url":callback_url,
        "selling_price":selling_price,
        "TotalCartItems":TotalCartItems,
        "data":Payu_data,
    }
    return render(request, 'checkout.html', context)












from django.core.mail import EmailMultiAlternatives

from django.template.loader import get_template
from datetime import datetime
@csrf_exempt
def handlerequest(request):
    if request.method == 'POST':
        try:
            transaction_id = request.POST.get("txnid")
            mihpayid = request.POST.get("mihpayid")
            hash = request.POST.get("hash")
            mode = request.POST.get("mode")
            status = request.POST.get("status")

            product = [p for p in CartItem.objects.all() if p.transaction_id==transaction_id and p.availability==True ]

            print("product", product)

            for order_db in product:
                order_db.mihpayid=mihpayid
                order_db.hash=hash
                order_db.save()

                print("inside for loop", order_db.mihpayid)
                print("inside for loop", order_db.hash)

                            
            if status == 'success':
                order_db = [p for p in CartItem.objects.all() if p.transaction_id==transaction_id and p.availability==True ]
                print("status", status)

        except:
            return HttpResponse("third 505 Not Found")
        
    context={
        "transaction_id":transaction_id,
        "mihpayid":mihpayid,
        "status":status,
        "mode":mode,
    }
    return render(request, "transaction_successfull.html", context)







 
        
# from datetime import datetime
# def payment_done(request):
#     user=request.user
    
#     mail_date = []
#     mail_order_id = []
#     mail_product_id = []
#     mail_product_title = []
#     mail_quantity = []
#     mail_total_cost = []

#     transaction_id = request.GET.get('transaction_id')
#     mihpayid = request.GET.get('mihpayid')
#     status = request.GET.get('status')
#     mode = request.GET.get('mode')

#     print("payment done == mihpayid", mihpayid)
#     print("payment done == transaction_id", transaction_id, "type", type(transaction_id))
#     print("payment done == status", status)
#     print("payment done == mode", mode)
#     print("payment done == user", user)
    
#     if status == 'success':
#         order_db = [p for p in CartItem.objects.all() if p.user==request.user and p.transaction_id==transaction_id and p.mihpayid==mihpayid and p.availability==True ]
        
#         for order_db in order_db:
#             address=Address.objects.get(id=order_db.address and user==request.user)
#             prod=Product.objects.get(id=order_db.product.id)

#             if prod.quantity >= order_db.quantity: 
#                 available_stock = prod.quantity-order_db.quantity
#                 prod.quantity = available_stock
#                 prod.save()
#             else:
#                 # Handle the error: maybe raise an exception or redirect with an error message
#                 return HttpResponse("Insufficient stock for product: " + prod.name)
                    
#             order_placed = Placed_Order(price=order_db.product.price, order_id=order_db.order_id, product_id_number=order_db.product_id_number, user=user, address=address, transaction_id=order_db.transaction_id, product=order_db.product, quantity=order_db.quantity, payment_status=1, mihpayid=order_db.mihpayid, hash=order_db.hash)
#             order_placed.save()

#             update= Order_Tracker(tracking_id=order_db.product_id_number, update_desc="The order has been placed", orderInfo=order_placed)
#             update.save()            
                        
#             mail_date.append(order_db.datetime)
#             mail_order_id.append(order_db.order_id)
#             mail_product_id.append(order_db.product_id_number)
#             mail_product_title.append(order_db.product.title)
#             mail_quantity.append(order_db.quantity)
#             mail_total_cost.append(order_db.product.price)
            
#             order_db.delete()

#     all_datetime=mail_date[0]
#     datetime_string=str(all_datetime)
#     order_datetime=datetime.fromisoformat(datetime_string)
#     order_date=order_datetime.date()
#     total=0
#     email=address.email
#     house_no=address.house_no
#     area=address.area
#     city=address.city
#     state=address.state
#     pincode=address.pincode
#     circle = "\u25E6"
#     disc = "\u25CF"
#     product_info = []
#     for i in range(len(mail_product_title)):
#         # info = f" {disc} {mail_product_id[i]} - {mail_product_title[i]} - {mail_quantity[i]} x Rs{mail_total_cost[i]:.2f} = Rs{mail_quantity[i]*mail_total_cost[i]:.2f}"
#         info = f" {disc} {mail_product_title[i]} - {mail_quantity[i]} x Rs{mail_total_cost[i]:.2f} = Rs{mail_quantity[i]*mail_total_cost[i]:.2f}"
#         total += mail_quantity[i]*mail_total_cost[i]
#         product_info.append(info)

#     template1 = f"Dear {address.full_name} \n\nThank you for your recent purchase from our store. We are pleased to confirm that your order has been received and is being processed. Below are the details of your order: \n\nOrder ID: {mail_order_id[0]}\nDate of Purchase: {order_date}\n\n"
#     template2 = "Order Summary:\n{}"
#     template3 = template2.format('\n'.join(product_info))
#     template4 = f"\n {disc} Shipping: 70INR\n {disc} Taxes: Rs6.00\n {disc} Total: Rs{total}\n\nShipping Information:\n{address.full_name}\n{house_no}, {area}\n{city}, {state} {pincode}\nDelivery Method: Standard Shipping\nEstimated Delivery Date: March 30, 2023\n\nPayment Information:\nPayment Method: {mode}\nTotal Amount Paid: Rs{70+total}\n\nContact Information:\nIf you have any questions or concerns about your order, please do not hesitate to contact us at 1-800-123-4567 or support@livingstoneinstitute.com.\n\nCancellation and Return Policy:\nYou can cancel your order within 24 hours of placing it. If you are not completely satisfied with your purchase, you can return it for a full refund within 07 days.\n\nThank you for choosing our store. We appreciate your business and hope to see you again soon.\n\nSincerely,\nLivingstone Luxury Team."
    
#     template5=template1+template3+template4

#     send_mail(
#         f'Order Confirmation: {mail_order_id[0]} from JTPL STORE',
        
#         template5,

#         'nisha@johnnette.com',
#         [f'{email}'],
#         fail_silently=False,
#     )     
#     return redirect("/orders")










 
        
from datetime import datetime
import easypost
# easypost.api_key = settings.EASYPOST_API_KEY
def payment_done(request):
    user=request.user

    # Create EasyPost shipment
    # to_address = easypost.Address.create(
    #     name=address.full_name,
    #     street1=address.house_no + ", " + address.area,
    #     city=address.city,
    #     state=address.state,
    #     zip=address.pincode,
    #     country="IN",
    #     phone="9999999999"  # Optional
    # )
    

    # from_address = easypost.Address.create(
    #     company="JohnnetteStore",
    #     street1="123 Main St",
    #     city="Mumbai",
    #     state="MH",
    #     zip="400001",
    #     country="IN",
    #     phone="18001234567"
    # )

    # parcel = easypost.Parcel.create(
    #     length=10,
    #     width=5,
    #     height=4,
    #     weight=500  # in grams
    # )

    # shipment = easypost.Shipment.create(
    #     to_address=to_address,
    #     from_address=from_address,
    #     parcel=parcel
    # )

    # # Buy the cheapest rate
    # shipment.buy(rate=shipment.lowest_rate())

    # tracking_code = shipment.tracking_code
    # label_url = shipment.postage_label.label_url

    mail_date = []
    mail_order_id = []
    mail_product_id = []
    mail_product_title = []
    mail_quantity = []
    mail_total_cost = []

    transaction_id = request.GET.get('transaction_id')
    mihpayid = request.GET.get('mihpayid')
    status = request.GET.get('status')
    mode = request.GET.get('mode')


    if status == 'success':
        order_db = [p for p in CartItem.objects.all() if p.user==request.user and p.transaction_id==transaction_id and p.mihpayid==mihpayid and p.availability==True ]
        
        # orders = [
        #     item for item in CartItem.objects.all()
        #     if item.user == user and item.transaction_id == transaction_id and item.mihpayid == mihpayid and item.availability
        # ]

        for order_db in order_db:
            address=Address.objects.get(id=order_db.address and user==request.user)
            prod=Product.objects.get(id=order_db.product.id)

            if prod.quantity >= order_db.quantity: 
                available_stock = prod.quantity-order_db.quantity
                prod.quantity = available_stock
                prod.save()
            else:
                # Handle the error: maybe raise an exception or redirect with an error message
                return HttpResponse("Insufficient stock for product: " + prod.name)
                    
            order_placed = Placed_Order(
                price=order_db.product.price, 
                order_id=order_db.order_id, 
                product_id_number=order_db.product_id_number, 
                user=user, 
                address=address, 
                transaction_id=order_db.transaction_id, 
                product=order_db.product, 
                quantity=order_db.quantity, 
                payment_status=1, 
                mihpayid=order_db.mihpayid, 
                hash=order_db.hash
                )
            order_placed.save()

            
            # EasyPost shipment
            try:
                to_address = easypost.Address.create(
                    name=address.full_name,
                    street1=f"{address.house_no}, {address.area}",
                    city=address.city,
                    state=address.state,
                    zip=address.pincode,
                    country="IN",
                    phone="9999999999"
                )

                from_address = easypost.Address.create(
                    company="JohnnetteStore",
                    street1="123 Main St",
                    city="Mumbai",
                    state="MH",
                    zip="400001",
                    country="IN",
                    phone="18001234567"
                )

                parcel = easypost.Parcel.create(
                    length=10,
                    width=6,
                    height=4,
                    weight=500  
                )

                shipment = easypost.Shipment.create(
                    to_address=to_address,
                    from_address=from_address,
                    parcel=parcel
                )

                # Buy label with cheapest rate
                shipment.buy(rate=shipment.lowest_rate())

                # Save tracking info in order (add these fields in model if not present)

            except Exception as e:
                print("EasyPost error:", e)

            update= Order_Tracker(tracking_id=order_db.product_id_number, update_desc="The order has been placed", orderInfo=order_placed)
            update.save()            
                        
            mail_date.append(order_db.datetime)
            mail_order_id.append(order_db.order_id)
            mail_product_id.append(order_db.product_id_number)
            mail_product_title.append(order_db.product.title)
            mail_quantity.append(order_db.quantity)
            mail_total_cost.append(order_db.product.price)
            
            order_db.delete()

    all_datetime=mail_date[0]
    datetime_string=str(all_datetime)
    order_datetime=datetime.fromisoformat(datetime_string)
    order_date=order_datetime.date()
    total=0
    email=address.email
    house_no=address.house_no
    area=address.area
    city=address.city
    state=address.state
    pincode=address.pincode
    circle = "\u25E6"
    disc = "\u25CF"
    product_info = []
    for i in range(len(mail_product_title)):
        # info = f" {disc} {mail_product_id[i]} - {mail_product_title[i]} - {mail_quantity[i]} x Rs{mail_total_cost[i]:.2f} = Rs{mail_quantity[i]*mail_total_cost[i]:.2f}"
        info = f" {disc} {mail_product_title[i]} - {mail_quantity[i]} x Rs{mail_total_cost[i]:.2f} = Rs{mail_quantity[i]*mail_total_cost[i]:.2f}"
        total += mail_quantity[i]*mail_total_cost[i]
        product_info.append(info)

    template1 = f"Dear {address.full_name} \n\nThank you for your recent purchase from our store. We are pleased to confirm that your order has been received and is being processed. Below are the details of your order: \n\nOrder ID: {mail_order_id[0]}\nDate of Purchase: {order_date}\n\n"
    template2 = "Order Summary:\n{}"
    template3 = template2.format('\n'.join(product_info))
    template4 = f"\n {disc} Shipping: 70INR\n {disc} Taxes: Rs6.00\n {disc} Total: Rs{total}\n\nShipping Information:\n{address.full_name}\n{house_no}, {area}\n{city}, {state} {pincode}\nDelivery Method: Standard Shipping\nEstimated Delivery Date: March 30, 2023\n\nPayment Information:\nPayment Method: {mode}\nTotal Amount Paid: Rs{70+total}\n\nContact Information:\nIf you have any questions or concerns about your order, please do not hesitate to contact us at 1-800-123-4567 or support@livingstoneinstitute.com.\n\nCancellation and Return Policy:\nYou can cancel your order within 24 hours of placing it. If you are not completely satisfied with your purchase, you can return it for a full refund within 07 days.\n\nThank you for choosing our store. We appreciate your business and hope to see you again soon.\n\nSincerely,\nLivingstone Luxury Team."
    
    template5=template1+template3+template4

    send_mail(
        f'Order Confirmation: {mail_order_id[0]} from JTPL STORE',
        
        template5,

        'nisha@johnnette.com',
        [f'{email}'],
        fail_silently=False,
    )     
    return redirect("/orders")

# ======x====== PayUmoney integration =======x======
# ======x====== PayUmoney integration ==============






# @csrf_exempt   
def payment_failed(request):
    TotalCartItems=0
    if request.user.is_authenticated:
        TotalCartItems = len(CartItem.objects.filter(user=request.user))

    context={
        "TotalCartItems":TotalCartItems,
    }
    return render(request, "transaction_failed.html", context)
        
        
        




@login_required(login_url="/login")
def orders(request):
    TotalCartItems=0
    if request.user.is_authenticated:
        TotalCartItems = len(CartItem.objects.filter(user=request.user))
    op=Placed_Order.objects.filter(user=request.user).order_by('-id')
    return render(request, 'orders.html', {"order_placed":op, "TotalCartItems":TotalCartItems})





# def search(request):
#     TotalCartItems=0
#     if request.user.is_authenticated:
#         TotalCartItems = len(Cart_Item.objects.filter(user=request.user))

#     query = request.GET['query']

#     if len(query)>78:
#         products = Product.objects.none()
#     elif not query:
#         products = Product.objects.none()
#     else:
#         excluded_categories = Q(category__icontains="HIDE") | Q(category__icontains="FEATURED")
#         ProductTitle = Product.objects.filter(product_title__icontains=query).exclude(excluded_categories)
#         ProductBrand = Product.objects.filter(brand_name__icontains=query).exclude(excluded_categories)
#         ProductDiscription = Product.objects.filter(product_discription__icontains=query).exclude(excluded_categories)
#         products = ProductTitle.union(ProductDiscription).union(ProductBrand)
        
#     paginator = Paginator(products,10)
#     page_number = request.GET.get('page')
#     SearchFinalData = paginator.get_page(page_number)
#     total_pages = SearchFinalData.paginator.num_pages
#     page_list = [n+1 for n in range(total_pages)]
    
    
#     cart_item_list=[]
#     if request.user.is_authenticated:
#         cart_item = Cart_Item.objects.filter(user=request.user)
    
#         for c in cart_item:
#             cart_item_list.append(c.product.id)
        
#     context={
#         "products":products,
#         "cart_item":cart_item_list,
#         "query":query,
#         "TotalCartItems":TotalCartItems,
#         "SearchFinalData":SearchFinalData,
#         "total_pages":total_pages,
#         "page_list":page_list,
#     }
#     return render(request, 'app/search.html', context)








from django.http import JsonResponse
def tracker(request):
    TotalCartItems=0
    if request.user.is_authenticated:
        TotalCartItems = len(CartItem.objects.filter(user=request.user))

    if request.method == "POST":
        productId = request.POST.get('prod_id')
        tracking_id = productId

        print(productId)
        try:
            order = Placed_Order.objects.filter(product_id_number=productId)
            if len(order) > 0:
                update = Order_Tracker.objects.filter(tracking_id=productId)

            for order in order:
                pass
            
        except:
            return HttpResponse("None")
    context = {
        "update": update,
        "order":order,
        "tracking_id":tracking_id,
        "TotalCartItems":TotalCartItems,
    }
    return render(request, 'tracker.html', context)




@login_required
def checkout_final(request):
    user_cart = CartItem.objects.filter(user=request.user)

    # Validate and deduct stock
    for item in user_cart:
        if item.product.quantity < item.quantity:
            return JsonResponse({'error': f"Insufficient stock for {item.product.title}"}, status=400)

    for item in user_cart:
        item.product.quantity -= item.quantity
        item.product.save()

   
    user_cart.delete()

    return JsonResponse({'message': 'Checkout successful'})




#  to save order history 
@login_required
def load_order_history_section(request):
    orders = Order.objects.filter(user=request.user).prefetch_related('items__product')
    return render(request, 'my_order.html', {'orders': orders})









# view for checkout/billing address





def billing_address_view(request):
    guest_email = request.session.get("guest_email", None)
    if not guest_email:
        return redirect("guest_checkout")

    default_address = Address.objects.filter(user=request.user, is_default=True).first()

    return render(request, "billing_address.html", {
        "guest_email": guest_email,
        "default_address": default_address,
        "user": request.user
    })







# view for address management

@login_required
def address_list_view(request):
    addresses = Address.objects.filter(user=request.user)
    return render(request, 'address_list.html', {'addresses': addresses})

@login_required
def add_address_view(request):
    if request.method == 'POST':
        form = AddressForm(request.POST)
        if form.is_valid():
            address = form.save(commit=False)
            address.user = request.user
            address.save()
            return redirect('address_list')
        else:
            print(form.errors)  
    else:
        form = AddressForm()
    return render(request, 'address_form.html', {'form': form, 'action': 'Add'})


# for address edit
@login_required
def edit_address_view(request, pk):
    address = get_object_or_404(Address, pk=pk, user=request.user)
    if request.method == 'POST':
        form = AddressForm(request.POST, instance=address)
        if form.is_valid():
            form.save()
            return redirect('address_list')
    else:
        form = AddressForm(instance=address)
    return render(request, 'address_form.html', {'form': form, 'action': 'Edit'})

# for adddress delete
@login_required
def delete_address_view(request, pk):
    address = get_object_or_404(Address, pk=pk, user=request.user)
    address.delete()
    return redirect('address_list')






def Deliveryaddress(request):
    form = AddressForm() 

    if request.method == "POST":
        form = AddressForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('some-success-url')  

    addresses = Address.objects.all() 
    return render(request, 'deliveryaddress.html', {'form': form, 'add': addresses})