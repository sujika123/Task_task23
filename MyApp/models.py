from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class Login(AbstractUser):
    is_user = models.BooleanField(default=False)

class userlogin(models.Model):
    user = models.ForeignKey(Login,on_delete = models.CASCADE,related_name = 'user',null=True)
    name = models.CharField(max_length=50)
    address = models.TextField(max_length=200)
    phone = models.IntegerField()

    def __str__(self):
        return self.name

class task(models.Model):
    user = models.ForeignKey(Login, on_delete=models.CASCADE)
    Title = models.CharField(max_length=100)
    Description = models.TextField(max_length=100)
    DueDate = models.DateField()
    Category = models.CharField(max_length=150)

    def __str__(self):
        return self.Title

