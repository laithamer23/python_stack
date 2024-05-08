from django.shortcuts import render
from time import gmtime, strftime

def index(req):
    return render(req,"index.html")




    
def index(request):
    context = {
        "time": strftime(" %H:%M %p", gmtime()),
        "date": strftime("%B %d,%y", gmtime())
        
    }
    return render(request,'index.html', context)


