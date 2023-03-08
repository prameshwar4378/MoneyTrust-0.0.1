
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms  import AuthenticationForm
from django import forms
from .models import DB_Loan,DB_Become_Partner,DB_Enquiry

class login_form(AuthenticationForm):
    username=forms.CharField(label='username')
    password=forms.CharField(label='Password')



class Form_Loan_Application(forms.ModelForm):
    class Meta:
        model = DB_Loan
        fields='__all__'
        widgets={
            'first_name':forms.TextInput(attrs={'class':'form-control','placeholder':'First Name'}),
            'last_name':forms.TextInput(attrs={'class':'form-control','placeholder':'Last Name'}),
            'pin_code':forms.TextInput(attrs={'class':'form-control','placeholder':'Pin Code'}),
            'mobile':forms.TextInput(attrs={'class':'form-control','placeholder':'Mobile Number'}),
            'income':forms.TextInput(attrs={'class':'form-control','placeholder':'Income'}),
            'emp_type':forms.Select(attrs={'class':'form-control'}),
            'loan_amount':forms.TextInput(attrs={'class':'form-control','placeholder':'Loan Amount'}),
            'salary_received':forms.Select(attrs={'class':'form-control'}),
        }


class Form_Become_Partner(forms.ModelForm):
    class Meta:
        model = DB_Become_Partner
        fields='__all__'
        widgets={
            'first_name':forms.TextInput(attrs={'class':'form-control','placeholder':'First Name'}),
            'last_name':forms.TextInput(attrs={'class':'form-control','placeholder':'Last Name'}),
            'mobile':forms.TextInput(attrs={'class':'form-control','placeholder':'Mobile Number'}),
            'email':forms.TextInput(attrs={'class':'form-control','placeholder':'Email'}),
            'city':forms.Select(attrs={'class':'form-control'}),
            'pan':forms.TextInput(attrs={'class':'form-control','placeholder':'PAN No'}),
            'profession':forms.Select(attrs={'class':'form-control'}),
        }


class Form_Enquiry(forms.ModelForm):
    class Meta:
        model = DB_Enquiry
        fields='__all__'
        widgets={
            'first_name':forms.TextInput(attrs={'class':'form-control','placeholder':'First Name'}),
            'last_name':forms.TextInput(attrs={'class':'form-control','placeholder':'Last Name'}),
            'mobile':forms.TextInput(attrs={'class':'form-control','placeholder':'Mobile Number'}),
            'email':forms.TextInput(attrs={'class':'form-control','placeholder':'Email'}),
            'city':forms.Select(attrs={'class':'form-control'}),
            'reason':forms.Select(attrs={'class':'form-control'}),
            'subject':forms.TextInput(attrs={'class':'form-control','placeholder':'Subject'}), 
            'message':forms.Textarea(attrs={'class':'form-control','placeholder':'Message'}), 
        }
