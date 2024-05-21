from django.shortcuts import render, redirect
from .models import User 
from django.contrib import messages
import bcrypt



def index(request):
    context={
        'data':User.objects.all()
    }
  
    return render(request, "index.html",context)


def Registration(request):
    
    errors = User.objects.basic_validator(request.POST)
     
    if len(errors) > 0:
      
        for key, value in errors.items():
            messages.error(request, value)

        return redirect('/')
    else:

        request.session['first_name'] =request.POST['first_name']
        last_name=request.POST['last_name']
        email=request.POST['email']
        password=request.POST['password']
      
        User.objects.create(first_name = request.session['first_name'], last_name = last_name, email = email , password =  bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode())
        return redirect('/success')
          

def success(request):

    return render(request,"success.html")  

def login(request):
    user = User.objects.filter(username=request.POST['username']) 
    if user: 
        logged_user = user[0]
        if bcrypt.checkpw(request.POST['password'].encode(), logged_user.password.encode()):
            request.session['userid'] = logged_user.id
            return redirect('/success')
        

    
   
