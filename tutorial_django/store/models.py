from ast import Mod
from pyexpat import model
from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=255)


class Product(models.Model):
    sku = models.CharField(max_length=10, primary_key=True)
    title = models.CharField(max_length=255) 
    description = models.TextField()
    price = models.DecimalField(max_digit=5, decimal_places=2)
    inventory = models.IntegerField()
    last_update = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)


class Customer(models.Model):
    MEMBERSHIP_BRONZE = 'B'
    MEMBERSHIP_SILVER = 'S'
    MEMBERSHIP_GOLD = 'G'

    MEMBERSHIP_CHOICES = [
        (MEMBERSHIP_BRONZE, 'Bronze'), 
        (MEMBERSHIP_SILVER, 'Silver'), 
        (MEMBERSHIP_GOLD, 'Gold'), 
    ] 

    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=255)
    birth_date = models.DateField(null=True)
    membership = models.CharField(max_length=1, choices=MEMBERSHIP_CHOICES, default=MEMBERSHIP_BRONZE)


class Address(models.Model):
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)


class Order(models.Model):
    ORDER_STATUS_PENDING = 'P'
    ORDER_STATUS_FAILED = 'F'
    ORDER_STATUS_COMPLETE = 'C'

    ORDER_STATUS_CHOICES = [
        (ORDER_STATUS_PENDING, 'Pending'),
        (ORDER_STATUS_FAILED, 'Failed'),
        (ORDER_STATUS_COMPLETE, 'Complete'),
    ]

    placed_at = models.DateTimeField(auto_now_add=True)
    order_status = models.CharField(max_length=1, choices=ORDER_STATUS_CHOICES, default=ORDER_STATUS_PENDING)
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT)


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.PROTECT)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    quantity = models.PositiveSmallIntegerField()
    unit_price = models.DecimalField(max_digit=5, decimal_places=2)


class Cart(models.Model):
    create_at = models.DateTimeField(auto_now_add=True)


class CartItem(models.Model):
    cart = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField()