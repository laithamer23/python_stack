from django.shortcuts import render,redirect
from .models import Users

def index(request):
     user={

          'hat' : Users.objects.all()
     }
     return render(request,"index.html",user)


def add_users(request):
     fname=request.POST['fname']
     lname=request.POST['lname']
     email=request.POST['email']
     age=request.POST['age']
     Users.objects.create(firstname = fname , lastname = lname , email_address = email , age = age)
     return redirect('/')
