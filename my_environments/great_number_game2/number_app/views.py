from django.shortcuts import render	,HttpResponse
def index(request):
    return render(request, "index.html")


import random 	             
random.randint(1, 100) 

def number(request):
    if request.method == "POST":
        number = random.randint(1, 100) 
        number_from_form = int(request.POST['number'])
    if number_from_form == number:
    
     return HttpResponse(f'number is {number}')
    
    elif number_from_form < number:
       return HttpResponse('to low')
    
    else:
       return HttpResponse('to hight')
     
    
