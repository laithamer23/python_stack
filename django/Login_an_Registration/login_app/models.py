from django.db import models
import re

class UserManager(models.Manager):

    def basic_validator(self, postData):
        errors = {}
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if len(postData['first_name']) < 2 or not str.isalpha(postData['first_name']):
            errors['first_name'] = ' fisrt name should be at least 2 characters'

        if len(postData['last_name']) < 2 or not str.isalpha(postData['last_name']):
             errors['last_name'] = 'last name should be at least 2 characters'

            
        if not EMAIL_REGEX.match(postData['email']):               
            errors['email'] = 'Invalid email address!'

        if len(postData['password']) < 8:
             errors['password'] = ' password should be at least 8 characters'
             
        if postData['confirm_pw'] != postData['password']:
             errors['confirm_pw'] = 'Password don,t match'
        return errors
    

class User(models.Model):
    first_name=models.CharField(max_length=2)
    last_name=models.CharField(max_length=2)
    email=models.CharField(max_length=8)
    password=models.CharField(max_length=8)
    confirm_pw=models.CharField(max_length=8)
    created_at = models.DateTimeField(auto_now_add = True,null=True)
    updated_at = models.DateTimeField(auto_now = True)
    objects=UserManager()



    
