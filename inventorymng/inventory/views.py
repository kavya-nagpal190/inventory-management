from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework import viewsets, generics
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.db.models import Sum, F
from inventory.serializers import ProductSerializer, SalesSerializer, RegisterSerializer
from inventory.models import Product, Sales

class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]

class ProductViewSet(viewsets.ModelViewSet):
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['price', 'quantity']
    search_fields = ['name']
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]

    @action(detail=False, methods=['get'])
    def low_stock(self, request):
        threshold = int(request.query_params.get('threshold', 10))
        products = Product.objects.filter(quantity__lte=threshold)
        serializer = self.get_serializer(products, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['get'])
    def revenue(self, request, pk=None):
        product = self.get_object()
        total = Sales.objects.filter(product_sold=product).aggregate(
            revenue=Sum(F('quantity_sold') * F('product_sold__price'))
        )
        return Response({
            'product': product.name,
            'total_revenue': total['revenue'] or 0
        })

    @action(detail=True, methods=['get'])
    def sales_history(self, request, pk=None):
        product = self.get_object()
        sales = Sales.objects.filter(product_sold=product)
        serializer = SalesSerializer(sales, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['get'])
    def top_selling(self, request):
        limit = int(request.query_params.get('limit', 5))
        products = Product.objects.annotate(
            total_sold=Sum('sales__quantity_sold')
        ).order_by('-total_sold')[:limit]
        serializer = self.get_serializer(products, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['post'])
    def restock(self, request, pk=None):
        product = self.get_object()
        quantity = int(request.data.get('quantity', 0))
        if quantity <= 0:
            return Response({'error': 'Quantity must be greater than 0'}, status=400)
        product.quantity += quantity
        product.save()
        return Response({
            'product': product.name,
            'new_quantity': product.quantity
        })

class SalesViewSet(viewsets.ModelViewSet):
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['quantity_sold', 'date']
    search_fields = ['product_sold__name']
    queryset = Sales.objects.all()
    serializer_class = SalesSerializer
    permission_classes = [IsAuthenticated]

    @action(detail=False, methods=['get'])
    def summary(self, request):
        total_revenue = Sales.objects.aggregate(
            revenue=Sum(F('quantity_sold') * F('product_sold__price'))
        )
        return Response(total_revenue)

    @action(detail=False, methods=['get'])
    def revenue_by_date(self, request):
        start = request.query_params.get('start')
        end = request.query_params.get('end')
        sales = Sales.objects.all()
        if start:
            sales = sales.filter(date__gte=start)
        if end:
            sales = sales.filter(date__lte=end)
        total = sales.aggregate(
            revenue=Sum(F('quantity_sold') * F('product_sold__price')),
            total_sold=Sum('quantity_sold')
        )
        return Response(total)