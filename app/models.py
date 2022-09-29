from django.db import models

class Firm(models.Model):
    name = models.CharField(max_length=120, blank=True)

class User(models.Model):
    name = models.CharField(max_length=120, blank=True)
    email = models.CharField(max_length=120, blank=True)
    firm = models.ForeignKey(Firm, on_delete=models.CASCADE)
    