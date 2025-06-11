from django.core.management.base import BaseCommand, CommandError
from inventory.models import Item
import csv, json


class Command(BaseCommand):
    help = "Migrates the data from the sheets_data folder into the database"

    def handle(self, *args, **options):
        Item.objects.all().delete() # Delete existing database entiries

        # Get list of room file names + CSV path
        lines = open('inventory/static/sheets_data/rooms.json','r').read() # Read data from json
        files = json.loads(lines)

        for f in files: # Loop through each room
            with open(f['path'],'r') as file:
                room = f['name']
                
                reader = csv.DictReader(file) # Get CSV data as dictionary

                for line in reader: # Loop through each item
                    print(line,room)

                    # Add item to the database
                    Item.objects.create(
                        name=line['Item'],
                        quantity=line['Quantity'],
                        location=line['Location'],
                        notes=line['Notes'],
                        room=room)