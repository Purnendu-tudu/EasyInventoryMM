from django.urls import path

from .views import index , inventory_list

urlpatterns = [
    path("",index, name="index"),
    path("inventorylist/", inventory_list, name="inventoryList")
]
 
