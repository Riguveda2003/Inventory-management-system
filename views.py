# inventory/views.py  

from django.shortcuts import render, redirect  
from .models import Product, Supplier, SaleOrder, StockMovement  
from .forms import SupplierForm, ProductForm, SaleOrderForm  

def add_product(request):  
    if request.method == 'POST':  
        form = ProductForm(request.POST)  
        if form.is_valid():  
            form.save()  
            return redirect('list_product')  
    else:  
        form = ProductForm()  
    return render(request, 'add_product.html', {'form': form})  

def list_products(request):  
    products = Product.objects.all()  
    return render(request, 'list_products.html', {'products': products})  

def add_supplier(request):  
    if request.method == 'POST':  
        form = SupplierForm(request.POST)  
        if form.is_valid():  
            form.save()  
            return redirect('list_suppliers')  
    else:  
        form = SupplierForm()  
    return render(request, 'add_supplier.html', {'form': form})  

def list_suppliers(request):  
    suppliers = Supplier.objects.all()  
    return render(request, 'list_suppliers.html', {'suppliers': suppliers})  

def create_sale_order(request):  
    if request.method == 'POST':  
        form = SaleOrderForm(request.POST)  
        if form.is_valid():  
            sale_order = form.save(commit=False)  
            sale_order.total_price = sale_order.product.price * sale_order.quantity  
            sale_order.save()  
            # Logic to update stock levels and add stock movement  
            product = sale_order.product  
            product.stock_quantity -= sale_order.quantity  
            product.save()  
            StockMovement.objects.create(product=product, quantity=sale_order.quantity, movement_type='Out')  
            return redirect('list_sales_orders')  
    else:  
        form = SaleOrderForm()  
    return render(request, 'create_sale_order.html', {'form': form})  

def list_sales_orders(request):  
    sales_orders = SaleOrder.objects.all()  
    return render(request, 'list_sales_orders.html', {'sales_orders': sales_orders})
