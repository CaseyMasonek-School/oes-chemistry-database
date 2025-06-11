import csv
import sqlite3
from django.contrib import admin

from .models import Item

# Register your models here.

@admin.register(Item) # Register model to the admin site
class ItemAdmin(admin.ModelAdmin):
    list_display = ["name"] # Display the name in the list of items