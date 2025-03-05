from django.db import models
from django.urls import reverse

class ProductType(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(default="No description available.")
    
    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=255)
    product_type = models.ForeignKey(
        ProductType,
        on_delete=models.SET_NULL,
        null = True
    )
    description = models.TextField(default="No description available.")
    price = models.DecimalField(max_digits=63, decimal_places=2)
    
    class Meta:
        ordering = ['name']
    
    def __str__(self):
        return f'{self.name} of type {self.product_type}'

    def get_absolute_url(self):
        return reverse('merchstore:product_detail', args=[self.pk])
