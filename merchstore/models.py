from django.db import models
from django.urls import reverse

from user_management.models import Profile


class ProductType(models.Model):
    """
    A class for a type of product
    """

    name = models.CharField(max_length=255)
    description = models.TextField(default="No description available.")

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Product(models.Model):
    """
    A class for a product
    """

    name = models.CharField(max_length=255)
    product_type = models.ForeignKey(
        ProductType,
        on_delete=models.SET_NULL,
        null=True
    )
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE)
    description = models.TextField(default="No description available.")
    price = models.DecimalField(max_digits=63, decimal_places=2)
    stock = models.PositiveIntegerField()

    AVAILABLE = "available"
    ONSALE = "on_sale"
    OUTOFSTOCK = "out_of_stock"

    STATUS_CHOICES = (
        (AVAILABLE, "Available"),
        (ONSALE, "On Sale"),
        (OUTOFSTOCK, "Out of Stock"),
    )

    status = models.CharField(max_length=20,
                              choices=STATUS_CHOICES,
                              default=AVAILABLE)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return f'{self.name} of type {self.product_type}'

    def get_absolute_url(self):
        return reverse('merchstore:product_detail', args=[self.pk])


class Transaction(models.Model):
    """
    A class for transactions of products
    """

    buyer = models.ForeignKey(Profile,
                              on_delete=models.SET_NULL,
                              null=True,
                              related_name='transactions')
    product = models.ForeignKey(Product,
                                on_delete=models.SET_NULL,
                                null=True,
                                related_name='transactions')
    amount = models.PositiveIntegerField()

    ONCART = "on_cart"
    TOPAY = "to_pay"
    TOSHIP = "to_ship"
    TORECEIVE = "to_receive"
    DELIVERED = "delivered"

    STATUS_CHOICES = (
        (ONCART, "On Cart"),
        (TOPAY, "To Pay"),
        (TOSHIP, "To Ship"),
        (TORECEIVE, "To Receive"),
        (DELIVERED, "Delivered"),
    )

    status = models.CharField(max_length=20, choices=STATUS_CHOICES)

    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.buyer} bought {self.product}'
