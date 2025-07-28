from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ValidationError
from phonenumber_field.modelfields import PhoneNumberField
from datetime import date
from datetime import timedelta
from django.utils import timezone

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_verified = models.BooleanField(default=False)
    otp = models.CharField(max_length=6, blank=True)

    def __str__(self):
        return self.user.username




# for user profile details save

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    gender = models.CharField(max_length=20, blank=True)
    mobile = models.CharField(max_length=15, blank=True)
    phone = models.CharField(max_length=15, blank=True)
    first_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return f"{self.user.username} Profile"



countries = (('AF', 'AFGHANISTAN'),('AL', 'ALBANIA'),('DZ', 'ALGERIA'),('AS', 'AMERICAN SAMOA'),('AD', 'ANDORRA'),('AO', 'ANGOLA'),('AI', 'ANGUILLA'),('AQ', 'ANTARCTICA'),('AG', 'ANTIGUA AND BARBUDA'),('AR', 'ARGENTINA'),('AM', 'ARMENIA'),('AW', 'ARUBA'),('AU', 'AUSTRALIA'),('AT', 'AUSTRIA'),('AZ', 'AZERBAIJAN'),('BS', 'BAHAMAS'),('BH', 'BAHRAIN'),('BD', 'BANGLADESH'),('BB', 'BARBADOS'),('BY', 'BELARUS'),('BE', 'BELGIUM'),('BZ', 'BELIZE'),('BJ', 'BENIN'),('BM', 'BERMUDA'),('BT', 'BHUTAN'),('BO', 'BOLIVIA'),('BA', 'BOSNIA AND HERZEGOVINA'),('BW', 'BOTSWANA'),('BV', 'BOUVET ISLAND'),('BR', 'BRAZIL'),('IO', 'BRITISH INDIAN OCEAN TERRITORY'),('BN', 'BRUNEI DARUSSALAM'),('BG', 'BULGARIA'),('BF', 'BURKINA FASO'),('BI', 'BURUNDI'),('KH', 'CAMBODIA'),('CM', 'CAMEROON'),('CA', 'CANADA'),('CV', 'CAPE VERDE'),('KY', 'CAYMAN ISLANDS'),('CF', 'CENTRAL AFRICAN REPUBLIC'),('TD', 'CHAD'),('CL', 'CHILE'),('CN', 'CHINA'),('CX', 'CHRISTMAS ISLAND'),('CC', 'COCOS (KEELING) ISLANDS'),('CO', 'COLOMBIA'),('KM', 'COMOROS'),('CG', 'CONGO'),('CD', 'CONGO, THE DEMOCRATIC REPUBLIC OF'),('CK', 'COOK ISLANDS'),('CR', 'COSTA RICA'),('CI', "CÃ”TE D'IVOIRE"),('HR', 'CROATIA'),('CU', 'CUBA'),('CY', 'CYPRUS'),('CZ', 'CZECH REPUBLIC'),('DK', 'DENMARK'),('DJ', 'DJIBOUTI'),('DM', 'DOMINICA'),('DO', 'DOMINICAN REPUBLIC'),('EC', 'ECUADOR'),('EG', 'EGYPT'),('SV', 'EL SALVADOR'),('GQ', 'EQUATORIAL GUINEA'),('ER', 'ERITREA'),('EE', 'ESTONIA'),('ET', 'ETHIOPIA'),('FK', 'FALKLAND ISLANDS (MALVINAS)'),('FO', 'FAROE ISLANDS'),('FJ', 'FIJI'),('FI', 'FINLAND'),('FR', 'FRANCE'),('GF', 'FRENCH GUIANA'),('PF', 'FRENCH POLYNESIA'),('TF', 'FRENCH SOUTHERN TERRITORIES'),('GA', 'GABON'),('GM', 'GAMBIA'),('GE', 'GEORGIA'),('DE', 'GERMANY'),('GH', 'GHANA'),('GI', 'GIBRALTAR'),('GR', 'GREECE'),('GL', 'GREENLAND'),('GD', 'GRENADA'),('GP', 'GUADELOUPE'),('GU', 'GUAM'),('GT', 'GUATEMALA'),('GN', 'GUINEA'),('GW', 'GUINEA'),('GY', 'GUYANA'),('HT', 'HAITI'),('HM', 'HEARD ISLAND AND MCDONALD ISLANDS'),('HN', 'HONDURAS'),('HK', 'HONG KONG'),('HU', 'HUNGARY'),('IS', 'ICELAND'),('IN', 'INDIA'),('ID', 'INDONESIA'),('IR', 'IRAN, ISLAMIC REPUBLIC OF'),('IQ', 'IRAQ'),('IE', 'IRELAND'),('IL', 'ISRAEL'),('IT', 'ITALY'),('JM', 'JAMAICA'),('JP', 'JAPAN'),('JO', 'JORDAN'),('KZ', 'KAZAKHSTAN'),('KE', 'KENYA'),('KI', 'KIRIBATI'),('KP', "KOREA, DEMOCRATIC PEOPLE'S REPUBLIC OF"),('KR', 'KOREA, REPUBLIC OF'),('KW', 'KUWAIT'),('KG', 'KYRGYZSTAN'),('LA', "LAO PEOPLE'S DEMOCRATIC REPUBLIC"),('LV', 'LATVIA'),('LB', 'LEBANON'),('LS', 'LESOTHO'),('LR', 'LIBERIA'),('LY', 'LIBYAN ARAB JAMAHIRIYA'),('LI', 'LIECHTENSTEIN'),('LT', 'LITHUANIA'),('LU', 'LUXEMBOURG'),('MO', 'MACAO'),('MK', 'MACEDONIA, THE FORMER YUGOSLAV REPUBLIC OF'),('MG', 'MADAGASCAR'),('MW', 'MALAWI'),('MY', 'MALAYSIA'),('MV', 'MALDIVES'),('ML', 'MALI'),('MT', 'MALTA'),('MH', 'MARSHALL ISLANDS'),('MQ', 'MARTINIQUE'),('MR', 'MAURITANIA'),('MU', 'MAURITIUS'),('YT', 'MAYOTTE'),('MX', 'MEXICO'),('FM', 'MICRONESIA, FEDERATED STATES OF'),('MD', 'MOLDOVA, REPUBLIC OF'),('MC', 'MONACO'),('MN', 'MONGOLIA'),('MS', 'MONTSERRAT'),('MA', 'MOROCCO'),('MZ', 'MOZAMBIQUE'),('MM', 'MYANMAR'),('NA', 'NAMIBIA'),('NR', 'NAURU'),('NP', 'NEPAL'),('NL', 'NETHERLANDS'),('AN', 'NETHERLANDS ANTILLES'),('NC', 'NEW CALEDONIA'),('NZ', 'NEW ZEALAND'),('NI', 'NICARAGUA'),('NE', 'NIGER'),('NG', 'NIGERIA'),('NU', 'NIUE'),('NF', 'NORFOLK ISLAND'),('MP', 'NORTHERN MARIANA ISLANDS'),('NO', 'NORWAY'),('OM', 'OMAN'),('PK', 'PAKISTAN'),('PW', 'PALAU'),('PS', 'PALESTINIAN TERRITORY, OCCUPIED'),('PA', 'PANAMA'),('PG', 'PAPUA NEW GUINEA'),('PY', 'PARAGUAY'),('PE', 'PERU'),('PH', 'PHILIPPINES'),('PN', 'PITCAIRN'),('PL', 'POLAND'),('PT', 'PORTUGAL'),('PR', 'PUERTO RICO'),('QA', 'QATAR'),('RE', 'RÃ‰UNION'),('RO', 'ROMANIA'),('RU', 'RUSSIAN FEDERATION'),('RW', 'RWANDA'),('SH', 'SAINT HELENA'),('KN', 'SAINT KITTS AND NEVIS'),('LC', 'SAINT LUCIA'),('PM', 'SAINT PIERRE AND MIQUELON'),('VC', 'SAINT VINCENT AND THE GRENADINES'),('WS', 'SAMOA'),('SM', 'SAN MARINO'),('ST', 'SAO TOME AND PRINCIPE'),('SA', 'SAUDI ARABIA'),('SN', 'SENEGAL'),('CS', 'SERBIA AND MONTENEGRO'),('SC', 'SEYCHELLES'),('SL', 'SIERRA LEONE'),('SG', 'SINGAPORE'),('SK', 'SLOVAKIA'),('SI', 'SLOVENIA'),('SB', 'SOLOMON ISLANDS'),('SO', 'SOMALIA'),('ZA', 'SOUTH AFRICA'),('GS', 'SOUTH GEORGIA AND SOUTH SANDWICH ISLANDS'),('ES', 'SPAIN'),('LK', 'SRI LANKA'),('SD', 'SUDAN'),('SR', 'SURINAME'),('SJ', 'SVALBARD AND JAN MAYEN'),('SZ', 'SWAZILAND'),('SE', 'SWEDEN'),('CH', 'SWITZERLAND'),('SY', 'SYRIAN ARAB REPUBLIC'),('TW', 'TAIWAN, PROVINCE OF CHINA'),('TJ', 'TAJIKISTAN'),('TZ', 'TANZANIA, UNITED REPUBLIC OF'),('TH', 'THAILAND'),('TL', 'TIMOR'),('TG', 'TOGO'),('TK', 'TOKELAU'),('TO', 'TONGA'),('TT', 'TRINIDAD AND TOBAGO'),('TN', 'TUNISIA'),('TR', 'TURKEY'),('TM', 'TURKMENISTAN'),('TC', 'TURKS AND CAICOS ISLANDS'),('TV', 'TUVALU'),('UG', 'UGANDA'),('UA', 'UKRAINE'),('AE', 'UNITED ARAB EMIRATES'),('GB', 'UNITED KINGDOM'),('US', 'UNITED STATES'),('UM', 'UNITED STATES MINOR OUTLYING ISLANDS'),('UY', 'URUGUAY'),('UZ', 'UZBEKISTAN'),('VU', 'VANUATU'),('VN', 'VIET NAM'),('VG', 'VIRGIN ISLANDS, BRITISH'),('VI', 'VIRGIN ISLANDS, U.S.'),('WF', 'WALLIS AND FUTUNA'),('EH', 'WESTERN SAHARA'),('YE', 'YEMEN'),('ZW', 'ZIMBABWE'))

state = (("AN","Andaman and Nicobar Islands"),("AP","Andhra Pradesh"),("AR","Arunachal Pradesh"),("AS","Assam"),("BR","Bihar"),("CG","Chhattisgarh"),("CH","Chandigarh"),("DN","Dadra and Nagar Haveli"),("DD","Daman and Diu"),("DL","Delhi"),("GA","Goa"),("GJ","Gujarat"),("HR","Haryana"),("HP","Himachal Pradesh"),("JK","Jammu and Kashmir"),("JH","Jharkhand"),("KA","Karnataka"),("KL","Kerala"),("LA","Ladakh"),("LD","Lakshadweep"),("MP","Madhya Pradesh"),("MH","Maharashtra"),("MN","Manipur"),("ML","Meghalaya"),("MZ","Mizoram"),("NL","Nagaland"),("OD","Odisha"),("PB","Punjab"),("PY","Pondicherry"),("RJ","Rajasthan"),("SK","Sikkim"),("TN","Tamil Nadu"),("TS","Telangana"),("TR","Tripura"),("UP","Uttar Pradesh"),("UK","Uttarakhand"),("WB","West Bengal")) 




def validate_pincode(value):
    if len(str(value)) != 6:
        raise ValidationError("Pincode must be exactly 6 digits")



# for save user address home/ office
from phonenumber_field.modelfields import PhoneNumberField

class Address(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=200)
    email = models.EmailField(max_length=256)
    mobile_number = PhoneNumberField(region=None, blank=True)
    house_no = models.CharField(max_length=250)
    area = models.CharField(max_length=250)
    landmark = models.CharField(max_length=250)
    locality = models.CharField(max_length=200)
    city = models.CharField(max_length=50)
    state = models.CharField(choices=state, max_length=50)
    pincode = models.IntegerField(validators=[validate_pincode])
    home = models.BooleanField(default=False)
    office = models.BooleanField(default=False)
    is_default = models.BooleanField(default=False)


    def __str__(self):
        return str(self.id)








# model for product listing

from django.db import models

class Product(models.Model):
    CATEGORY_CHOICES = [
        ('men', 'Men'),
        ('women', 'Women'),
        ('accessories', 'Accessories'),
        ('home_decor', 'Home Decor'),
    ]

    SUBCATEGORY_CHOICES = [
    # Men
    ('tshirt', 'T-Shirt'),
    ('wallet', 'Wallet'),
    ('belt_men', 'Belt'),

    # Women
    ('women_tshirt', 'women tshirt'),
    ('bag', 'Bag'),
    ('women_belt', 'Women Belt'),

    # Accessories (used under "men" too)
    ('accessory_belt', 'Belt'),
    ('accessory_wallet', 'Wallet'),
    ('accessory_caps', 'Caps'),  
    ('accessory_beer_mug', 'Beer Mug'),

    # Home Decor
    ('candles', 'Candles'),
]

    SIZE_CHOICES = [
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
        ('XL', 'Extra Large'),
    ]

    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    color = models.CharField(max_length=100, blank=True, null=True)
    size = models.CharField(max_length=10, choices=SIZE_CHOICES, blank=True, null=True)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)





    # add for inventorhy management
    quantity = models.PositiveIntegerField(default=0, blank=True, null=True)
    subcategory = models.CharField(max_length=30, choices=SUBCATEGORY_CHOICES)

    description = models.TextField(blank=True, null=True)
    delivery_info = models.TextField(blank=True, null=True)
    payment_info = models.TextField(blank=True, null=True)

    image1 = models.ImageField(upload_to='products/')
    image2 = models.ImageField(upload_to='products/', blank=True, null=True)
    image3 = models.ImageField(upload_to='products/', blank=True, null=True)
    image4 = models.ImageField(upload_to='products/', blank=True, null=True)

    is_new = models.BooleanField(default=False)

    def __str__(self):
        return self.title




# model for inventory management

from django.contrib.auth.models import User

class CartItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    order_id = models.CharField(max_length=10000000, null=True, blank=True, default=None) 
    product_id_number=models.CharField(max_length=255, unique=True, default=None, blank=True, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    added_at = models.DateTimeField(auto_now_add=True)
    availability=models.BooleanField(default=False)
    address = models.CharField(max_length=100, null=True, blank=True, default=None)
    datetime = models.DateTimeField(default=timezone.now)
    transaction_id = models.CharField(max_length=10000000, null=True, blank=True)
    mihpayid = models.CharField(max_length=10000000, null=True, blank=True)
    hash = models.CharField(max_length=10000000, null=True, blank=True)

    def __str__(self):
        return f"{self.user.username} - {self.product.title} x {self.quantity}"
    


from .models import CartItem

@login_required
def checkout(request):
    cart_items = CartItem.objects.select_related('product').filter(user=request.user, availability=False)

    total = sum(item.product.price * item.quantity for item in cart_items)

    return render(request, 'checkout.html', {
        'cart_items': cart_items,
        'total': total,
    })






STATUS_CHOICES = (
    ('Pending', 'Pending'),
    ('Accepted', 'Accepted'),
    ('Packed', 'Packed'),
    ('On The Way', 'On The Way'),
    ('Deliverd', 'Deliverd'),
    ('Cancelled', 'Cancelled'),
)

payment_status_choices = (
    (1, 'Success'),
    (2, 'Failed'),
    (3, 'Pending'),
)

class Placed_Order(models.Model):
    id= models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # address = models.ForeignKey(Address, on_delete=models.CASCADE)
    address = models.ForeignKey('livingstone_app.Address', on_delete=models.CASCADE)
    product=models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    status = models.CharField(choices=STATUS_CHOICES, max_length=50, default="Pending")
    price = models.FloatField(blank=True, null=True)
    payment_status = models.IntegerField(choices = payment_status_choices, default=3)
    product_id_number=models.CharField(max_length=255, unique=True, default=None, blank=True, null=True)
    order_id = models.CharField(max_length=10000000, null=True, blank=True, default=None) 
    datetime_of_payment = models.DateTimeField(default=timezone.now)
    transaction_id = models.CharField(max_length=10000000, null=True, blank=True)
    mihpayid = models.CharField(max_length=10000000, null=True, blank=True)
    hash = models.CharField(max_length=10000000, null=True, blank=True)

    def __str__(self):
        return str(self.product)
    
    # def save(self, *args, **kwargs):
    #     if not self.expected_delivery_date:
    #         self.expected_delivery_date = self.datetime_of_payment + timedelta(days=7)
        
    #     if not self.offer:
    #         off = (self.actual_price-self.selling_price)/self.actual_price
    #         self.offer = round(off * 100, 2)
        
    #     super().save(*args, **kwargs)




class Order_Tracker(models.Model):
    orderInfo = models.ForeignKey(Placed_Order, on_delete=models.CASCADE, null=True, blank=True)
    update_id= models.AutoField(primary_key=True)
    tracking_id= models.CharField(max_length=90000)
    update_desc= models.CharField(max_length=5000)
    timestamp= models.DateField(auto_now_add= True)

    def __str__(self): 
        return self.update_desc[0:7] + "..."
    





# model for order history save

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    order_id = models.CharField(max_length=100, unique=True)
    address = models.ForeignKey(Address, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    paid_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    payment_method = models.CharField(max_length=50, default='Credit Card')
    payment_details = models.CharField(max_length=100, default='Card ending with 0000')

    def __str__(self):
        return self.order_id

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    quantity = models.PositiveIntegerField()
    size = models.CharField(max_length=10, blank=True)
    delivery_status = models.CharField(max_length=50, default="In - Transit")
    expected_delivery = models.DateField()

    def __str__(self):
        return f"{self.product.title} x {self.quantity}"



