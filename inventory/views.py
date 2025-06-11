from django.shortcuts import render, HttpResponse
from django.forms.models import model_to_dict
from django.template import loader

from .models import Item



def index(request):
    """ Returns a list of items in the inventory based on user filters """

    # Load template
    template = loader.get_template("index.html")

    # Get data for the form
    rooms = Item.objects.values('room').distinct()

    context = {
        'rooms': rooms,
    }

    return HttpResponse(template.render(context,request))

def show(request, item_id):
    """ Display all information about a single item """
    
    # Get item by id
    item = Item.objects.get(id=item_id)

    # Load template
    template = loader.get_template("show.html")

    context = {
        'name': item.name,
        'item': model_to_dict(item,exclude=['id','name']) # Return model as dict
    }

    return HttpResponse(template.render(context,request))

def filtered(request):
    """ Return a filtered version  """

    # Query params
    room_query = request.GET.get('room')
    name_query = request.GET.get('name')

    items = Item.objects.all() # Get all items

    # Filter results
    if room_query:
        items = items.filter(room=room_query)

    if name_query:
        items = items.filter(name__contains=name_query)
    else:
        name_query = ""

    # Load template
    template = loader.get_template("filtered.html")

    context = {
        'items': items,
    }

    return HttpResponse(template.render(context,request))