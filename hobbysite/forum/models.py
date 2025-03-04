from django.db import models
from django.urls import reverse

# Create your models here.
class ProductType(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField

    class Meta:
        ordering = ['name'] # Order by name in ascending order
    
    def __str__(self):
        return str(self.name)

class Product(models.Model):
    name = models.CharField(max_length=255)
    product_type = models.ForeignKey(
        ProductType,
        on_delete=models.SET_NULL,
        null=True,
    )
    description = models.TextField
    price = models.DecimalField(max_digits=63, decimal_places=2)

    class Meta:
        ordering = ['name'] # Order by name in ascending order
    
    def __str__(self):
        return f'{self.name} of type {self.product_type}'
    
    def get_absolute_url(self):
        return reverse('forum:product-detail', args=[self.pk])