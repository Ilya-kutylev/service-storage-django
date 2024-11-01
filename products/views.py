from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response

from .models import ProductType, ProductPrice, Product
from .serializers import ProductTypeSerializer, ProductPriceSerializer, ProductSerializer
from .services import reduce_stock


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
        """
        Уменьшает остаток товара на складе.
        Параметры запроса: {quantity: количество для уменьшения}
        """
        product = self.get_object()
        serializer = self.serializer_class(data=request.data, partial=True)

        # Проверка валидности данных через сериализатор
        serializer.is_valid(raise_exception=True)
        quantity_to_reduce = serializer.validated_data['quantity']

        try:
            # Вызов сервиса для уменьшения остатков товара на складе
            reduce_stock(product, quantity_to_reduce)
            return Response({'message': "Stock reduced successfully", 'remaining_stock': product.quantity},
                            status=status.HTTP_200_OK)
        except ValidationError as e:
            return Response({'detail': str(e)}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
