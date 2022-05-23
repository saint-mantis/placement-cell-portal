from django import forms
from .models import Students,Companies
from django.forms import ModelForm




class StudentsForm(forms.ModelForm):
     def __init__(self, *args, **kwargs):
         kwargs.setdefault('label_suffix', '')
         super(StudentsForm, self).__init__(*args, **kwargs)
         self.fields['name'].widget.attrs.update({'id':'','class': '','placeholder':'name'})
         self.fields['email'].widget.attrs.update({'id':'','class': '','placeholder':'email'})
         self.fields['phone'].widget.attrs.update({'id':'','class': '','placeholder':'phone'})
         self.fields['address'].widget.attrs.update({'id':'','class': '','placeholder':'address'})
         self.fields['password'].widget.attrs.update({'id':'','class': '','placeholder':'password'})
    
     class Meta:
        model = Students
        labels = {
            'name': '',
            'email': '',
            'phone': '',
            'address': '',
            'password': '',
            
        }
        fields = ['name','email','phone','address','password']

class LoginForm(forms.ModelForm):
     def __init__(self, *args, **kwargs):
         kwargs.setdefault('label_suffix', '')
         super(LoginForm, self).__init__(*args, **kwargs)
         self.fields['name'].widget.attrs.update({'id':'','class': '','placeholder':'name'})
         self.fields['password'].widget.attrs.update({'id':'','class': '','placeholder':'password'})
    
     class Meta:
        model = Students
        labels = {
            'name': '',
            'password': '',
            
        }
        fields = ['name','password']

class CompanyForm(forms.ModelForm):
     def __init__(self, *args, **kwargs):
         kwargs.setdefault('label_suffix', '')
         super(CompanyForm, self).__init__(*args, **kwargs)
         self.fields['companyinput'].widget.attrs.update({'id':'','class': '','placeholder':'name'})

    
     class Meta:
        model = Students
        labels = {
            'companyinput': '',   
        }
        fields = ['companyinput']


class AddComapany(forms.ModelForm):
     def __init__(self, *args, **kwargs):
         kwargs.setdefault('label_suffix', '')
         super(AddComapany, self).__init__(*args, **kwargs)
         self.fields['addcompany'].widget.attrs.update({'id':'','class': '','placeholder':'name'})

    
     class Meta:
        model = Companies
        labels = {
            'addcompany': '', 
        }
        fields = ['addcompany']
