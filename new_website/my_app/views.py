from django.shortcuts import render,redirect,get_object_or_404
from .forms import LoginForm,CreateUserForm,CreateRecordForm
from django.contrib.auth import authenticate
from django.contrib.auth.models import auth
from django.contrib.auth.decorators import login_required
from .models import Record
from django.http import HttpResponse
from django.contrib import messages
from django.views.generic import ListView,UpdateView
from . import models

# Create your views here.

def index(request):
    return render(request,'index.html',)


def register(request):
    form=CreateUserForm()
    if request.method=='POST':
        form=CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Account created successfully!')
        else:
            form=CreateUserForm()
                
        return redirect('login')            
    context={'form':form}       
    return render(request,'register.html',context=context) 


def login(request):
    form=LoginForm()
    if request.method =='POST':
        form=LoginForm(request,data=request.POST)
        if form.is_valid():
            username=request.POST.get('username')
            password=request.POST.get('password')
            user=authenticate(request,username=username,password=password)
            if user is not None:
                auth.login(request,user)
                messages.success(request,'Login successfully')
            return redirect('dashboard')    
    context={'form':form}
    return render(request,'login.html',context=context)    


class dashboard(ListView):
    #context_object_name='anything'
    model=models.Record
    template_name='dashboard.html'
    # def dashboard(request):
#     my_record=Record.objects.all()
#     context={'record':my_record}
#     return render(request,'dashboard.html',context=context)
    


@login_required(login_url='login')
def createrecord(request):
    form=CreateRecordForm()
    if request.method=='POST':
        form=CreateRecordForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request,'User Created successfully')
        return redirect('dashboard') 
      
    context={'form':form}
    return render(request,'create_record.html',context)

def updaterecord(request,pk):

    record=Record.objects.get(id=pk)
    form=CreateRecordForm(instance=record)
    if request.method=='POST':
        form=CreateRecordForm(request.POST,instance=record)
        if form.is_valid():
               form.save()
               messages.success(request,'Record update successfully')   
        return redirect('dashboard')  
    context={'form':form}  
    return render(request,'update.html',context) 



# class updaterecord(UpdateView):
#     fields=('First_name','Last_name')
#     model=models.Record


def deleterecord(request,pk):
    form=Record.objects.get(id=pk)   
    form.delete()
    return redirect('dashboard') 
      

  

def logout(request):
    auth.logout(request)

    return redirect('login')

class template(ListView):
    model=models.Record
    template_name='register.html'



           