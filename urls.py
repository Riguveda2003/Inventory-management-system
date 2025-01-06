# inventory/urls.py  

from django.urls import path  
from .views import add_product, list_products, add_supplier, list_suppliers, create_sale_order, list_sales_orders  

urlpatterns = [  
    path('add-product/', add_product, name='add_product'),  
    path('products/', list_products, name='list_product'),  
    path('add-supplier/', add_supplier, name='add_supplier'),  
    path('suppliers/', list_suppliers, name='list_suppliers'),  
    path('create-sale-order/', create_sale_order, name='create_sale_order'),  
    path('sales-orders/', list_sales_orders, name='list_sales_orders'),  
]
