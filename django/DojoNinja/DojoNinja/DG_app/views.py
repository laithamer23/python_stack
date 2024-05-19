from django.shortcuts import render, redirect
from .models import Dojo,Ninja

def index(request):
    dojo={
        'adduserdojo':Dojo.objects.all()
    }

    ninja={
        'adduserninja':Ninja.objects.all()
    }
    return render(request,"index.html",dojo,ninja)
        
    



def insert_dojo(request):
    name=request.POST['name']
    city=request.POST['city']
    state=request.POST['state']
    Dojo.objects.create(name = name , city = city , state = state )
    return redirect ('/')



def insert_ninja(request):
    first_name=request.POST['lname']
    last_name=request.POST['fname']
    Ninja.objects.create(first_name=first_name , last_name=last_name)
    return redirect('/')


   