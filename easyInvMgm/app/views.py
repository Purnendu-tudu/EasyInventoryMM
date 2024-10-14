from django.shortcuts import get_object_or_404, render

from .models import Inventory

# Create your views here.

def index(request):
    context = {
        "title" : "Home"
    }
    return render(request, "inventory/index.html", context=context)


def inventory_list(request):
    inventories = Inventory.objects.all()

    context = {
        "title" : "Items List",
        "inventories" : inventories

    }

    return render(request, "inventory/inventory_list.html" , context=context)


def per_producut(request, pk):
    inventory = get_object_or_404(Inventory, pk=pk)
    context = {
        'inventory' : inventory
    }

    return render(request, "inventory/per_prodcut.html", context=context)