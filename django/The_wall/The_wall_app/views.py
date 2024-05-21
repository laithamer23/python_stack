from django.shortcuts import render,redirect
from .models import Users,Messages,Comments
from django.contrib import messages
import bcrypt

def index(request):
    context={
        'data':Users.objects.all(),
        'data':Messages.objects.all(),

    }
  
    return render(request, "index.html")




def Registration(request):
    
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
    

def wall(request):
    data={
        'messages':messages.objects.all()
    }
    return render(request,'wall.html',data)


def create_message(request,x):
    messages=request.POST['message']
    user=Users.objects.get(id=x)
    Messages.objects.create(message=messages,user=user)
    return redirect('/show')

def create_comment(request,x,w):
    comment=request.POST['comment']
    user=Users.objects.get(id=w)
    messages=Messages.objects.get(id=x)
    Comments.objects.create(comment=comment,user=user,message=messages)
    return redirect('/show')

          
