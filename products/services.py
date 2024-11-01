from rest_framework.exceptions import ValidationError
from .models import Product


# Функция уменьшающая остатки товара и проверяющая, что количество не меньше запрашиваемого
def reduce_stock(product: Product, quantity: int) -> bool:
    if product.quantity < quantity:
        raise ValidationError("Insufficient stock")

    product.quantity -= quantity
    product.save()
    return True
