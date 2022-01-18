from pickle import TRUE
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
    MEMBERSHIP_BRONZE= 'B'
    MEMBERSHIP_SILVER = 'S'
    MEMBERSHIP_GOLD = 'G'

    MEMBERSHIP_CHOICES = [
        (MEMBERSHIP_BRONZE,'Bronze'),
        (MEMBERSHIP_SILVER,'Silver'),
        (MEMBERSHIP_GOLD, 'Gold')
    ]

    first_name = models.CharField(max_length=255)
    last_name= models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=255)
    birth_date = models.DateField(null=True)
    membership = models.CharField(choices=MEMBERSHIP_CHOICES, default=MEMBERSHIP_BRONZE)

class Order(models.Model):
    PAYMENT_STATUS_PENDING = 'P'
    PAYMENT_STATUS_COMPLETE= 'C'
    PAYMENT_STATUS_FAILED = 'F'

    PAYMENT_STATUS_CHOICES = [
        (PAYMENT_STATUS_PENDING,'Pending'), 
        (PAYMENT_STATUS_COMPLETE, 'Complete'), 
        (PAYMENT_STATUS_FAILED,'Failed')
    ]

    place_at = models.DateTimeField(auto_now_add=True)
    payment_status = models.CharField(choices=PAYMENT_STATUS_CHOICES, default=PAYMENT_STATUS_PENDING)

class Address(models.Model):
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    #on_delete is the action that when the customer model is deleted, CASCADE means the address will be deleted too
    #SET_NULL, while the customer is deleted, the address will remain, the customer field will set to null
    #PROTECT, address (child) cannot be deleted, if the customer(parent) is exist, child can only be delete, while the cutsomer is deleted too
    customer = models.OneToOneField(Customer, on_delete=models.CASCADE, primary_key=TRUE)
    #we add primary key to the customer field, so each customer only has one address, one to one relationship valid