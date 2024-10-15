from django.urls import path

from .views import index , inventory_list, per_producut_view, add_product, delete_product, update_product, dashboard

urlpatterns = [
    path("",index, name="index"),
    path("inventorylist/", inventory_list, name="inventoryList"),
    path("product/<int:pk>", per_producut_view, name="product" ),
    path("addProduct/",add_product, name="addProduct"),
    path("delete/<int:pk>",delete_product, name="deleteProduct"),
    path("update/<int:pk>",update_product, name="updateProduct"),
    path("dashboard/", dashboard, name="dashboard")

]
 
