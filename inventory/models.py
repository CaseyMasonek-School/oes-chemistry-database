from django.db import models

class Item(models.Model):
    """ This model represents an inventory item """
    
    name = models.CharField(max_length=100)
    quantity = models.CharField(max_length=100)
    room = models.CharField(max_length=100)
    location = models.CharField(max_length=100,blank=True)
    notes = models.TextField(blank=True)