from django import forms
from .models import Profile, Address 
from livingstone_app.models import Address 

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['gender', 'mobile', 'phone', 'first_name', 'last_name']





               
               
class CustomerAddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ['full_name', 'locality', 'mobile_number', 'email', 'house_no', 'area', 'landmark', 'city', 'state', 'pincode', 'home', 'office'] 
        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'form-control'}),
            'locality': forms.TextInput(attrs={'class': 'form-control'}),
            'mobile_number': forms.NumberInput(attrs={'class': 'form-control', "placeholder": "Enter valid contact number with country code (ex: +91 0000000000)"}),
            'email': forms.EmailInput(attrs={'class': 'form-control', "placeholder": "Enter valid Email address"}),
            'house_no': forms.TextInput(attrs={'class': 'form-control'}),
            'area': forms.TextInput(attrs={'class': 'form-control'}),
            'landmark': forms.TextInput(attrs={'class': 'form-control'}),
            'city': forms.TextInput(attrs={'class': 'form-control'}),
            'state': forms.Select(attrs={'class': 'form-control'}),
            'pincode': forms.NumberInput(attrs={'class': 'form-control'}),
            'home': forms.CheckboxInput(attrs={'class': 'fas fa-home-lg-alt'}),
            'office': forms.CheckboxInput(),
        }




# adjust address for dashboard page

from phonenumber_field.formfields import PhoneNumberField
from phonenumber_field.widgets import PhoneNumberPrefixWidget


class AddressForm(forms.ModelForm):
    mobile_number = PhoneNumberField(
       
        label="Mobile Number",
        required=True
    )

    class Meta:
        model = Address
        fields = [
            'full_name', 'locality', 'mobile_number', 'email',
            'house_no', 'area', 'landmark', 'city', 'state',
            'pincode', 'home', 'office'
        ]
        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'form-control'}),
            'locality': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'house_no': forms.TextInput(attrs={'class': 'form-control'}),
            'area': forms.TextInput(attrs={'class': 'form-control'}),
            'landmark': forms.TextInput(attrs={'class': 'form-control'}),
            'city': forms.TextInput(attrs={'class': 'form-control'}),
            'state': forms.Select(attrs={'class': 'form-control'}),
            'pincode': forms.NumberInput(attrs={'class': 'form-control'}),
            'home': forms.CheckboxInput(),
            'office': forms.CheckboxInput(),
        }




