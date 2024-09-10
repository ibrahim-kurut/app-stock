from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet, BrandViewSet, ProductViewSet, FirmViewSet, PurchasesViewSet, SalesViewSet

router = DefaultRouter()
router.register('categories', CategoryViewSet)
router.register('brands', BrandViewSet)
router.register('products', ProductViewSet)
router.register('firms', FirmViewSet)
router.register('purchases', PurchasesViewSet)
router.register('sales', SalesViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
