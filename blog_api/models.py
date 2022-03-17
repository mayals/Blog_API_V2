from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings



""" # https://docs.djangoproject.com/en/4.0/topics/auth/customizing/#substituting-a-custom-user-model"""
class UserModel(AbstractUser):
   username        = models.CharField(max_length = 50, null = True, unique = True)
   email           = models.EmailField(unique = True, null = True)
   first_name      = models.CharField(max_length = 10, null = True)
   last_name       = models.CharField(max_length = 10 ,null = True)
   born_date       = models.DateTimeField(null = True)
   USERNAME_FIELD  = 'username'
   REQUIRED_FIELDS = ['first_name', 'email']
   
   def __str__(self):
       return "{}".format(self.username) 





class Category(models.Model):
    name = models.CharField(max_length=32,blank=False,null=True,unique=True)
    
    def __str__(self):
        return self.name




class Post(models.Model):
    category   = models.ForeignKey(Category,on_delete=models.CASCADE, null=True, blank=False, related_name='posts')
    title      = models.CharField(max_length=100, null=True)
    author     = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,null=True,blank=False, related_name='posts')
    body       = models.TextField(null =True)
    created_at = models.DateTimeField(auto_now_add=True,null=True)
    updated_at = models.DateTimeField(auto_now=True,null=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering=['created_at']



     
