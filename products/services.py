from rest_framework.exceptions import ValidationError

from products.models import Product
from products.repositorys import ProductRepository


class ProductService:
    @staticmethod
    def reduce_stock(product_id: int, quantity: int) -> Product:
        """
        Reduces the remaining stock of goods in the warehouse.
        """
        product = ProductRepository.get_product_by_id(product_id)

        if product.quantity < quantity:
            raise ValidationError("Not enough stock available to reduce.")

        updated_product = ProductRepository.reduce_stock(product, quantity)
        return updated_product
