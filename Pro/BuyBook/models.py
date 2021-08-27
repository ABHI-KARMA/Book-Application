from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class AddBookModel(models.Model):
    id = models.BigAutoField(primary_key=True)
    bname = models.CharField(max_length=100)
    aname = models.CharField(max_length=100)
    price = models.CharField(max_length=10)

    def __str__(self):
        return "Name : {}".format(self.bname)

class createCustomer(models.Model):
    id = models.BigAutoField(primary_key=True)
    username = models.CharField(max_length=50,default='')
    pw = models.CharField(max_length=20,default='')
    fullname = models.CharField(max_length=50)
    number = models.CharField(max_length=20)
    email = models.EmailField()
    address = models.CharField(max_length=100)

    def __str__(self):
        return "Name : {}".format(self.fullname)

class Purchased(models.Model):
    id = models.BigAutoField(primary_key=True)
    bookname = models.CharField(max_length=100)
    authorname = models.CharField(max_length=100)
    price = models.CharField(max_length=10)
    
    def __str__(self):
        return "Book Name : {}".format(self.bookname)


