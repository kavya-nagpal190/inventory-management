from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=50)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    


class Sales(models.Model):
    product_sold = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity_sold = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):

     return self.product_sold.name
     
    
    