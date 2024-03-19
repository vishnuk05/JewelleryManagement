from django.db import models

# Create your models here.


class customer_table(models.Model):
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    age = models.IntegerField()
    phone = models.IntegerField()
    email = models.CharField(max_length=50)
    address = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images/',blank=True)
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    confirm_password = models.CharField(max_length=30)
    def __str__(self):
        return self.username
    



class staff_table(models.Model):
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    age = models.IntegerField()
    email = models.CharField(max_length=50)
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    confirm_password = models.CharField(max_length=30)
    approval = models.BooleanField(default=False)
    def __str__(self):
        return self.username


class contact_table(models.Model):
    name = models.CharField(max_length=20, blank=True,)
    email = models.CharField(max_length=50)
    inquiries =models.TextField() 
    def __str__(self):
        return self.email


class products(models.Model):
    product_name = models.CharField(max_length=50)
    price = models.IntegerField()
    material = models.CharField(max_length=20)
    category = models.CharField(max_length=20)
    image = models.ImageField(upload_to='images/',blank=True)
    def __str__(self):
        return self.product_name



