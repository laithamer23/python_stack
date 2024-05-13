from django.shortcuts import render,redirect
import random 

def index(request):
    if 'gold' not in request.session:
        request.session['gold'] = 0
    return render(request, "index.html")
    

def increase(request):
    increased = int(random.randint(10,20))
    request.session['gold'] += increased
    return redirect('/')




def dncrease(request):
    dncreased = int(random.randint(-50,50))
    request.session['gold'] += dncreased
    return redirect('/')




