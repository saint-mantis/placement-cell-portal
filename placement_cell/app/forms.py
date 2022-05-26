from django import forms
from .models import Students,Companies
from django.forms import ModelForm
import django_tables2 as tables




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
         self.fields['name'].widget.attrs.update({'id':'','class': 'bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500','placeholder':'Username'})
         self.fields['password'].widget.attrs.update({'id':'','class': 'bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500','placeholder':'Password'})
    
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
         self.fields['companyinput'].widget.attrs.update({'id':'','class': 'bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500','placeholder':'name'})

    
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
         self.fields['addcompany'].widget.attrs.update({'id':'','class': 'bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500','placeholder':'Add a Comapany'})

    
     class Meta:
        model = Companies
        labels = {
            'addcompany': '', 
        }
        fields = ['addcompany']


class Available(forms.ModelForm):
     def __init__(self, *args, **kwargs):
         kwargs.setdefault('label_suffix', '')
         super(Available, self).__init__(*args, **kwargs)
         self.fields['companyname'].widget.attrs.update({'id':'','class': 'bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500','placeholder':'Add a Comapany'})

    
     class Meta:
        model = Companies
        labels = {
            'companyname': '', 
        }
        fields = ['companyname']

