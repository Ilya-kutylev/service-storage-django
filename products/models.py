from django.core.validators import MinValueValidator
from django.db import models


class ProductType(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name="Title")
    description = models.TextField(verbose_name="Description")

    class Meta:
        verbose_name = "Type"
        verbose_name_plural = "Types"

    def __str__(self):
        return self.name


class ProductPrice(models.Model):
    currency = models.CharField(max_length=3, verbose_name="Currency")
    amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Amount")

    class Meta:
        verbose_name = "Price"
        verbose_name_plural = "Prices"

    def __str__(self):
        return f"{self.currency} {self.amount}"


class Product(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name="Title")
    quantity = models.PositiveIntegerField(validators=[MinValueValidator(1)], verbose_name="Quantity")
    barcode = models.CharField(max_length=13, verbose_name="Barcode")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated")
    price_id = models.ForeignKey(ProductPrice, on_delete=models.CASCADE, verbose_name="Price")
    type_id = models.ForeignKey(ProductType, on_delete=models.CASCADE, verbose_name="Type")

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"

    def __str__(self):
        return self.name
    