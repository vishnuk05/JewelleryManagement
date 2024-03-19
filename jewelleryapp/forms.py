from django import forms
from .models import *

class customer_form(forms.ModelForm):
    class Meta:
        model = customer_table

        fields = ('firstname','lastname','age','phone','address','email','image','username','password','confirm_password')
        
        widgets = {
            'firstname':forms.TextInput(attrs={'class':'form-control'}),
            'lastname':forms.TextInput(attrs={'class':'form-control'}),
            'age':forms.TextInput(attrs={'class':'form-control'}),
            'phone':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.TextInput(attrs={'class':'form-control'}),
            'address':forms.TextInput(attrs={'class':'form-control'}),
            'image':forms.FileInput(attrs={'class':'form-control'}),
            'username':forms.TextInput(attrs={'class':'form-control'}),
            'password':forms.TextInput(attrs={'class':'form-control'}),
            'confirm_password':forms.TextInput(attrs={'class':'form-control'}),
        }



class staff_form(forms.ModelForm):
    class Meta:
        model = staff_table

        fields = ('firstname','lastname','age','email','username','password','confirm_password','approval')
        
        widgets = {
            'firstname':forms.TextInput(attrs={'class':'form-control'}),
            'lastname':forms.TextInput(attrs={'class':'form-control'}),
            'age':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.TextInput(attrs={'class':'form-control'}),
            'username':forms.TextInput(attrs={'class':'form-control'}),
            'password':forms.TextInput(attrs={'class':'form-control'}),
            'confirm_password':forms.TextInput(attrs={'class':'form-control'}),
        }

class contact_form(forms.ModelForm):
    class Meta:
        model = contact_table

        fields = ('email','inquiries')

        widgets ={
            'email':forms.TextInput(attrs={'class':'form-control'}),
            'inquiries':forms.Textarea(attrs={'class':'form-control'})
        }

class product_form(forms.ModelForm):
    class Meta:
        model = products

        fields = ('product_name','price','material','category','image')

        widgets = {
            'product_name':forms.TextInput(attrs={'class':'form-control'}),
            'price':forms.NumberInput(attrs={'class':'form-control'}),
            'material':forms.TextInput(attrs={'class':'form-control'}),
            'category':forms.TextInput(attrs={'class':'form-control'}),
            'image':forms.FileInput(attrs={'class':'form-control'}),
        }