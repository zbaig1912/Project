from django.db import models

class Firm(models.Model):
    name = models.CharField(max_length=120, blank=True)

class User(models.Model):
    name = models.CharField(max_length=120, blank=True)
    email = models.CharField(max_length=120, blank=True)
    firm = models.ForeignKey(Firm, on_delete=models.CASCADE)

class Product(models.Model):
    name = models.CharField(max_length=120, blank=True)
    price = models.IntegerField()

class Transaction(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    total = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)