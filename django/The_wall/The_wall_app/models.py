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

class Users(models.Model):
    first_name=models.CharField(max_length=255)
    last_name=models.CharField(max_length=255)
    email=models.CharField(max_length=255)
    password=models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True,null=True)
    updated_at = models.DateTimeField(auto_now = True)
    objects=UserManager()

class Messages(models.Model):
    message=models.TextField(max_length=45)
    user = models.ForeignKey(Users, related_name='messages',on_delete=models.CASCADE,null=True)
    created_at = models.DateTimeField(auto_now_add = True,null=True)
    updated_at = models.DateTimeField(auto_now = True)

class Comments(models.Model):
    comment=models.TextField(max_length=45)
    user = models.ForeignKey(Messages,related_name='comments' ,on_delete=models.CASCADE,null=True)

    message = models.ForeignKey(Users, related_name='comments',on_delete=models.CASCADE,null=True)
    created_at = models.DateTimeField(auto_now_add = True,null=True)
    updated_at = models.DateTimeField(auto_now = True)

