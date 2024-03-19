from django.shortcuts import render , redirect
from .models import *
from .forms import *
from  django.contrib.auth import authenticate, login as log, logout
from django.contrib.auth.models import User, auth
from django.core.mail import send_mail

# Create your views here.


def home(request):
    return render(request,'home.html')

#################################################################################
def about(request):
    return render(request,'about.html')

##################################################################################
def contact(request):
    return render(request,'about.html')

###############################################################################################
def reg_customer(request):
    form =customer_form()
    if request.method =='POST':
        form =customer_form(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            email =form.cleaned_data['email']
            send_mail(
                'Login',
                'Login SUCCESSFULLY',
                'kvishnu5112@gmail.com',
                [email],
                fail_silently=False,
            )
            return redirect('cust_login')
    return render(request,'customer.html',{'form':form})


def cust_update(request,pk):
    pro = customer_table.objects.get(id=pk)
    form =customer_form(instance=pro)
    if request.method =='POST':
        form=customer_form(request.POST,instance=pro)
        if form.is_valid():
            form.save()
            return redirect('cust_dashboard')
    return render(request,'cust_update.html',{'form':form})

def cust_login(request):
    if request.method =='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        cr = customer_table.objects.filter(username=username,password=password)
        if cr:
            userdetails =customer_table.objects.get(username=username, password=password)
            id = userdetails.id
            username = userdetails.username
            password = userdetails.password
            request.session['id'] = id
            request.session['username']  = username
            request.session['password'] = password
            return redirect('cust_dashboard')
        else:
            error ='invalid credentails'
            return render(request, 'cust_login.html',{'error':error})
    else:
        return render(request,'cust_login.html')


def cust_dashboard(request):
    id=request.session['id']
    username= request.session['username']
    productsview = products.objects.all()
    return render(request,'cust_dashboard.html',{'id':id,'username':username,'productsview':productsview})

def cust_logout(request):
    logout(request)
    return redirect('cust_login')

###############################################################################################
def reg_staff(request):
    form =staff_form()
    if request.method =='POST':
        form =staff_form(request.POST,request.FILES)
        if form.is_valid():
            form.save()
    return render(request,'staff.html',{'form':form})

def staff_login(request):
    if request.method =='POST':
        username =request.POST.get('username')
        password =request.POST.get('password')
        stf =staff_table.objects.filter(username=username,password=password,approval=True)
        if stf:
            user_details=staff_table.objects.get(username=username,password=password)
            id= user_details.id
            username= user_details.username
            password=user_details.password
            request.session['id']=id
            request.session['username']=username
            request.session['password']=password
            return redirect('staff_dashboard')
        else:
            error='invalid credentials or not approved by admin yet'
            return render(request, 'staff_login.html', {'error':error})
    else:
        return render(request,'staff_login.html')


def staff_dashboard(request):
    id=request.session['id']
    username= request.session['username']
    form = product_form()
    if request.method =="POST":
        form = product_form(request.POST,request.FILES)
        if form.is_valid():
            form.save()
    cr = products.objects.all()
    return render(request,'staff_dashboard.html', {'username':username,'id':id,'form':form,'cr':cr})

def staff_logout(request):
    logout(request)
    return redirect('staff_login')


#image updated akunilla
def product_update(request,pk):
    pro = products.objects.get(id=pk)
    form =product_form(instance=pro)
    if request.method =='POST':
        form=product_form(request.POST, instance=pro)
        if form.is_valid():
            form.save()
            return redirect('staff_dashboard')
    return render(request, 'staff_productupdate.html',{'form':form})

def product_delete(request,pk):
    delete = products.objects.get(id=pk)
    delete.delete()
    return redirect('staff_dashboard')

###############################################################################################
def contact_info(request):
    form = contact_form()
    if request.method =="POST":
        form = contact_form(request.POST,request.FILES)
        if form.is_valid():
            form.save()
    return render(request,'contact.html',{'form':form})


##############################################cart ###################################
