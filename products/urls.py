from django.urls import path, include
from rest_framework.routers import DefaultRouter

from products.views import ProductViewSet, ProductPriceViewSet, ProductTypeViewSet

router = DefaultRouter()

# Регистрация всех ViewSet для моделей
router.register('products', ProductViewSet)
router.register('product-types', ProductTypeViewSet)
router.register('product-prices', ProductPriceViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
