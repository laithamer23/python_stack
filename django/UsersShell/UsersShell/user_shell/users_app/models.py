from django.db import models

class (models.Model):
     firstname = models.CharField(max_length=45)
     lastname = models.CharField(max_length=45)
     email_address = models.TextField()
     age = models.IntegerField()
     created_at = models.DateTimeField(auto_now_add=True)
     updated_at = models.DateTimeField(auto_now=True)

