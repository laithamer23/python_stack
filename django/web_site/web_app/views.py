from django.shortcuts import render
from .models import Movie,Actor,Category

def index(request):
    context={
        'movies':Movie.objects.all(),
        'actors':Actor.objects.all()

    }
    return render(request,'index.html',context)