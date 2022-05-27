from urllib import response
from django.shortcuts import render,redirect
from .models import Students,Companies
from .forms import StudentsForm,LoginForm,CompanyForm,AddComapany,Available
import django_tables2 as tables
from django.http import HttpResponse
from django.core import serializers
import json
import csv
from django.conf import settings
from pathlib import Path
import os
import pandas as pd

#rgb(182, 226, 242)


id = []
sessionid = []
listvar = []
user = []



def home(request):

    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        password = request.POST['password']
        internship = ['none']
        model = Students.objects.create(name=name,password=password,email=email,phone=phone,internship=internship)
        model.save()
        print("student added successful")
        msg = "User created Successfully, Login to Continue 👍"
        form = StudentsForm()
        context = {
               'form': form,
                'msg':msg
               }
        return render(request,'signup.html',context)
    form = StudentsForm()
    context = {
               'form': form,
                
               }
    return render(request, 'signup.html',context )

def login(request):
    if request.method == 'POST':
        name = request.POST['name']
        sessionid.clear()
        id.clear()
        id.append(name)
        sessionid.append(name)
        user.clear()
        user.append(name)

        
        print(f"array is {id}")
        password = request.POST['password']
        model = Students.objects.filter(name=name,password=password)

        if name == 'admin' and password == 'admin':
            addcompany = AddComapany()
            sessionid.clear()
            queryset=Students.objects.values('internship')
            print(queryset)
            return render(request,'admin.html',{'addcompany':addcompany})

        elif model:
            return redirect('apply')

        else:
            sessionid.clear()
            msg="Invalid username or password"
            context = {
               'login': LoginForm(),
               'msg':msg}
            return render(request,'login.html',context)
    context = {
               'login': LoginForm}
    return render(request,'login.html',context)

def apply(request):
    form = CompanyForm()
    if request.method == 'POST':
        print(request.POST)
        add= request.POST['companyinput']
        print(add)
        listvar.clear()
        listvar.append(add)
        print(listvar)
        print(id)
        authenticate = Companies.objects.filter(companyname=add)
        if authenticate:
            row = Students.objects.get(name = id[0])
            row.internship +=listvar
            row.save()
            form = CompanyForm()
            row = Students.objects.get(name = sessionid[0])
            internships = row.internship
            for i in internships:
                if "none" in internships:
                    internships.remove("none")
            print(internships)
            available = Companies.objects.values('companyname')
            username = user[0]
            return render(request,'home.html',{'form':form,'internships':internships,'available':available,'username':username})
        else:
            msg = f"The Company {add} is not available"
            row = Students.objects.get(name = sessionid[0])
            internships = row.internship
            available = Companies.objects.values('companyname')
            form = CompanyForm()
            username = user[0]
            return render(request,'home.html',{'form':form,'msg':msg,'internships':internships,'available':available,'username':username})
    print(f'session id is {sessionid}')
    row = Students.objects.get(name = sessionid[0])
    internships = row.internship
    for i in internships:
        if "none" in internships:
            internships.remove("none")
    print(internships)
    print(f'companies are {internships}')
    available = Companies.objects.values('companyname')
    username = user[0]
    return render(request,'home.html',{'form':form,'internships':internships,'available':available,'username':username})


def company(request):
    if request.method == 'POST':
        companyinput = request.POST['addcompany']
        print(companyinput)
        add = Companies.objects.create(companyname=companyinput)
        add.save()
        print("comapany added successfully")
        msg = "Comapany added Successfully"
    addcompany = AddComapany()
    return render(request,'admin.html',{'msg':msg,'addcompany':addcompany})

def download(request):
    if request.method == 'POST':
        students = Students.objects.all()
        response = HttpResponse('text/csv')
        response['Content-Disposition'] = 'attachment; filename=Student_Details.csv'
        writer = csv.writer(response)
        writer.writerow(['name','email','phone','password','internship'])
        for student in students:
            writer.writerow([student.name,student.email,student.phone,student.address,student.internship])
        return response
    addcompany = AddComapany()
    return render(request,'admin.html',{'addcompany':addcompany})









