from django.db import models

# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=30,unique=True)  #unique代表用户名唯一
    password = models.CharField(max_length=30)
    def __str__(self):
        return self.username

class User_Info(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name=models.CharField(max_length=4)
    qqnum=models.CharField(max_length=12)
    telnum=models.CharField(max_length=11)
    mailnum=models.EmailField(max_length=20)
    address=models.CharField(max_length=20)

    def __str__(self):
        return self.name