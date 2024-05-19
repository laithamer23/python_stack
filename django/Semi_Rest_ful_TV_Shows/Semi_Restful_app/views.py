
from django.shortcuts import render,redirect
from .models import show

def index(request):
    context={
        'show':show.objects.all()
    }
    return render(request, "show.html",context)

def create_user(request):
    title=request.POST['title']
    network=request.POST['network']
    release_date=request.POST['release_date']
    description=request.POST['description']

    show.objects.create(title=title,network=network,release_date=release_date,description=description)
    return redirect('/show')

def add_new(request):
    return render(request,'index.html')

def show2(request,x):
    showobject=show.objects.get(id=x)
    data={
    'id':showobject.id,
    'title':showobject.title,
    'release_date':showobject.release_date,
    'description':showobject.description,
    'updated_at':showobject.updated_at,
    'network':showobject.network
    }
    return render(request,'show2.html',data)

def delete(request,x):
    showobject=show.objects.get(id=x)
    showobject.delete()
    return redirect('/show')

def edit(request,x):
      showobject=show.objects.get(id=x)
      showobject.edit()
      return redirect('/show')


