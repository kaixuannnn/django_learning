from django.db import models

class Product(models.Model):
    #Django will always automatically create a primary key for us, as we want to crate key by our own can do as below
    #sku =  models.CharField(max_length=10, primary_key=True)
    title =  models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    inventory = models.IntegerField()
    #when there is update in Product Model, django automatically ipdate the last_update datetime
    last_update = models.DateField(auto_now=True)

class Customer(models.Model):
    first_name = models.CharField(max_length=255)
    last_name= models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=255)
    birth_date = models.DateField(null=True)
