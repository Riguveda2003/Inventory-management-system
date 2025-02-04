# inventory/models.py  

from django.db import models  

class Supplier(models.Model):  
    name = models.CharField(max_length=255)  
    email = models.EmailField()  
    phone = models.CharField(max_length=10)  
    address = models.TextField()  

    def __str__(self):  
        return self.name  

class Product(models.Model):  
    name = models.CharField(max_length=255)  
    description = models.TextField()  
    category = models.CharField(max_length=255)  
    price = models.DecimalField(max_digits=10, decimal_places=2)  
    stock_quantity = models.IntegerField()  
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)  

    def __str__(self):  
        return self.name  

class SaleOrder(models.Model):  
    product = models.ForeignKey(Product, on_delete=models.CASCADE)  
    quantity = models.IntegerField()  
    total_price = models.DecimalField(max_digits=10, decimal_places=2)  
    sale_date = models.DateField(auto_now_add=True)  
    status = models.CharField(max_length=20, choices=[('Pending', 'Pending'), ('Completed', 'Completed'), ('Cancelled', 'Cancelled')])  

class StockMovement(models.Model):  
    product = models.ForeignKey(Product, on_delete=models.CASCADE)  
    quantity = models.IntegerField()  
    movement_type = models.CharField(max_length=3, choices=[('In', 'In'), ('Out', 'Out')])  
    movement_date = models.DateField(auto_now_add=True)  
    notes = models.TextField(blank=True, null=True)
