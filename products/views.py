from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response

from products.models import ProductType, ProductPrice, Product
from products.services import ProductService
from products.serializers import ProductTypeSerializer, ProductPriceSerializer, ProductSerializer



class ProductTypeViewSet(viewsets.ModelViewSet):
    queryset = ProductType.objects.all()
    serializer_class = ProductTypeSerializer


class ProductPriceViewSet(viewsets.ModelViewSet):
    queryset = ProductPrice.objects.all()
    serializer_class = ProductPriceSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    @action(detail=True, methods=['patch'], url_path='reduce-stock')
    def reduce_stock(self, request, pk=None):
        serializer = self.serializer_class(data=request.data, partial=True)

        serializer.is_valid(raise_exception=True)
        quantity_to_reduce = serializer.validated_data['quantity']

        try:
            remaining_stock = ProductService.reduce_stock(pk, quantity_to_reduce)
            return Response({'message': "Stock reduced successfully", 'remaining_stock': remaining_stock.quantity},
                            status=status.HTTP_200_OK)
        except ValidationError as e:
            return Response({'detail': str(e)}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
