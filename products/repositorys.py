from django.core.exceptions import ObjectDoesNotExist, ValidationError
from django.db import transaction
from products.models import Product


class ProductRepository:
    @staticmethod
    def get_product_by_id(product_id: int):
        try:
            return Product.objects.get(id=product_id)
        except ObjectDoesNotExist:
            raise ValidationError("Product not found")

    @staticmethod
    @transaction.atomic
    def reduce_stock(product: Product, quantity: int):
        product.quantity =  quantity
        product.save(update_fields=["quantity"])
        product.refresh_from_db()
        return product
