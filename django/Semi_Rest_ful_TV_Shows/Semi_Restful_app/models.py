from django.db import models

class show(models.Model):
     
     title = models.CharField(max_length=255)
     network = models.CharField(max_length=255)
     release_date=models.DateField()
     description=models.TextField(null=True)
     created_at = models.DateTimeField(auto_now_add = True)
     updated_at = models.DateTimeField(auto_now = True)


