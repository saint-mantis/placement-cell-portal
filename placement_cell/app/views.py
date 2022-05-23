from django.shortcuts import render,redirect
from .models import Students,Companies
from .forms import StudentsForm,LoginForm,CompanyForm,AddComapany
namearray = []

def home(request):

    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        password = request.POST['password']
        model = Students.objects.create(name=name,password=password,email=email,phone=phone)
        model.save()


    form = StudentsForm()
    context = {
               'form': form}
    return render(request, 'index.html',context )

def login(request):
    if request.method == 'POST':
        name = request.POST['name']
        namearray.append(name)
        
        print(f"array is {namearray}")
        password = request.POST['password']
        model = Students.objects.filter(name=name,password=password)

        if name == 'admin' and password == 'admin':
            addcompany = AddComapany()
            table = Students.objects.all()
            #if request.method == 'POST':
                #print(request.POST)
                #companyinput = request.POST['addcompany']
                #add = Companies.objects.create(companyname=companyinput)
                #add.save()
                #print("comapany added successful")

            return render(request,'admin.html',{'table':table,'addcompany':addcompany})

        elif model:
            
            #row = Students.objects.get(name = "arun")
            
            #print(row.phone)
            #emp.name = 'Somename'
            #emp.save()
            #array = ['test4','test5','test6']
            #row.internship += array
            #row.save()
            #print(row.internship)
            return redirect('apply')

        else:
            context = {
               'login': LoginForm}
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
        listvar = []
        row = Students.objects.get(name = namearray[0])
        listvar.append('default')
        row.internship =listvar
        row.save()
        listvar.clear()
        listvar.append(add)
        print(listvar)
        print(namearray)
        #print(namearray[0])
        row = Students.objects.get(name = namearray[0])
        testarray=['test1','test2','test3']
        row.internship +=listvar
        row.save()
        namearray.clear()


    return render(request,'home.html',{'form':form})


def company(request):
    if request.method == 'POST':
        companyinput = request.POST['addcompany']
        print(companyinput)
        add = Companies.objects.create(companyname=companyinput)
        add.save()
        print("comapany added successful")
        msg = "comapany added successful"
    addcompany = AddComapany()
    return render(request,'admin.html',{'msg':msg,'addcompany':addcompany})







'''

emp = Employee.objects.get(pk = emp_id)
print(row.phone)
emp.name = 'Somename'
emp.save()
'''

     
'''{% for name in data %}
    
        <p>{{name.name}}</p>

    {% endfor %}'''