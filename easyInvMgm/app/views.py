from django.shortcuts import get_object_or_404, render, redirect

# here is the decoratores to prevent unauthorized access
from django.contrib.auth.decorators import login_required

from .models import Inventory

# here we are importing our forms
from .forms import AddInventoryForm, UpdateInventoryFrom




# Create your views here.

def index(request):
    context = {
        "title" : "Home"
    }
    return render(request, "inventory/index.html", context=context)

@login_required
def inventory_list(request):
    inventories = Inventory.objects.all()

    context = {
        "title" : "Items List",
        "inventories" : inventories

    }

    return render(request, "inventory/inventory_list.html" , context=context)

@login_required
def per_producut_view(request, pk):
    inventory = get_object_or_404(Inventory, pk=pk)
    context = {
        'inventory' : inventory
    }

    return render(request, "inventory/per_product.html", context=context)


@login_required
def add_product(request):
    if request.method == "POST":
        add_form = AddInventoryForm(data=request.POST)
        if add_form.is_valid():
            new_inventory = add_form.save(commit=False)
            new_inventory.sales = float(add_form.data['cost_per_item']) * float(add_form.data['quantity_sold'])
            new_inventory.save()
            return redirect("/inventory/inventorylist/")
    
    else:
        add_form = AddInventoryForm()

    context = {
        "form" : add_form
    }
    
    return render(request, "inventory/inventory_add.html", context=context )

@login_required
def delete_product(request, pk):
    inventory = get_object_or_404(Inventory, pk=pk)
    inventory.delete()
    return redirect("/inventory/inventorylist/")

@login_required
def update_product(request, pk):
    inventory = get_object_or_404(Inventory, pk=pk)

    if request.method == "POST":
        updateForm = UpdateInventoryFrom(data=request.POST)
        if updateForm.is_valid():
            inventory.name = updateForm.data['name']
            inventory.cost_per_item = updateForm.data['cost_per_item']
            inventory.quantity_in_stock = updateForm.data['quantity_in_stock']
            inventory.quantity_sold = updateForm.data['quantity_sold']
            inventory.sales = float(inventory.cost_per_item) * float(inventory.quantity_sold)
            inventory.save()
            return redirect("/inventory/inventorylist/")
    else:
        updateForm = UpdateInventoryFrom(instance=inventory)
    
    context = {
        "form" : updateForm
    }
    
    return render(request, "inventory/inventory_update.html", context=context)


    


