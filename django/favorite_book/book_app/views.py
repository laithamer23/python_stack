from django.shortcuts import render, redirect
from .models import Users,Books
from django.contrib import messages
import bcrypt

def index(request):
    context={
        'data':Users.objects.all(),
        'data':Books.objects.all()
    }
    return render (request,'index.html')


def registration(request):
        errors = Users.objects.basic_validator(request.POST)
     
        if len(errors) > 0:
      
            for key, value in errors.items():
                messages.error(request, value)

            return redirect('/')
        else:

            request.session['first_name'] =request.POST['first_name']
            last_name=request.POST['last_name']
            email=request.POST['email']
            password=request.POST['password']
      
        Users.objects.create(first_name = request.session['first_name'], last_name = last_name, email = email , password =  bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode())
        return redirect('/success')


def login(request):
  
        user = Users.objects.filter(email=request.POST['emails']) 
        if user: 
            logged_user = user[0] 
     
        if bcrypt.checkpw(request.POST['PW'].encode(), logged_user.password.encode()):
          
            request.session['userid'] = logged_user.id
         
            return redirect('/success')
  
        return redirect("/")


