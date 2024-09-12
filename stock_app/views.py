from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import Category, Brand, Product, Firm, Purchases, Sales
from .serializers import CategorySerializer, BrandSerializer, ProductSerializer, FirmSerializer, PurchasesSerializer, SalesSerializer

from rest_framework import filters

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
 # If the user does not work Login, it cannot do the following ['POST', 'PUT', 'PATCH', 'DELETE']
    def get_permissions(self):
        if self.request.method in ['POST', 'PUT', 'PATCH', 'DELETE']:
            return [IsAuthenticated()]
        return []


    # إضافة فلاتر البحث إلى الواجهة
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]  # دعم البحث والفلترة
    search_fields = ['name']  # حقل الاسم للبحث
    
    def get_queryset(self):
        # التحقق من وجود فلتر للاسم في طلب المستخدم
        name = self.request.query_params.get('name', None)
        if name:
            # فلترة الفئات بناءً على الاسم إذا تم توفيره
            return Category.objects.filter(name__icontains=name)
        return super().get_queryset()  # استرجاع جميع الفئات إذا لم يتم توفير فلتر

  

class BrandViewSet(viewsets.ModelViewSet):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer

    def get_permissions(self):
        if self.request.method in ['POST', 'PUT', 'PATCH', 'DELETE']:
            return [IsAuthenticated()]
        return []

 

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get_permissions(self):
        if self.request.method in ['POST', 'PUT', 'PATCH', 'DELETE']:
            return [IsAuthenticated()]
        return []

 

class FirmViewSet(viewsets.ModelViewSet):
    queryset = Firm.objects.all()
    serializer_class = FirmSerializer

    def get_permissions(self):
        if self.request.method in ['POST', 'PUT', 'PATCH', 'DELETE']:
            return [IsAuthenticated()]
        return []

 

class PurchasesViewSet(viewsets.ModelViewSet):
    queryset = Purchases.objects.all()
    serializer_class = PurchasesSerializer

    def get_permissions(self):
        if self.request.method in ['POST', 'PUT', 'PATCH', 'DELETE']:
            return [IsAuthenticated()]
        return []


class SalesViewSet(viewsets.ModelViewSet):
    queryset = Sales.objects.all()
    serializer_class = SalesSerializer

    def get_permissions(self):
        if self.request.method in ['POST', 'PUT', 'PATCH', 'DELETE']:
            return [IsAuthenticated()]
        return []

   

