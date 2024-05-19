from django.db import models

class Actor(models.Model):
    name=models.CharField(max_length=255)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    

 
class Category(models.Model):
    name=models.CharField(max_length=255)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)


class Movie(models.Model):
    title=models.CharField(max_length=45)
    description=models.TextField()
    url_image=models.TextField()
    category=models.ForeignKey(Category,related_name='movies', on_delete=models.CASCADE)
    actors=models.ManyToManyField(Actor,related_name='movies')
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    
