from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from . import models, serializers


class ProductCategoryViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = serializers.ProductCategorySerializer
    queryset = models.ProductCategory.objects.all()

    @action(methods=('GET',), detail=True)
    def products(self, request, pk):
        """Get all products by specific category."""
        products = models.Product.objects.filter(category__pk=pk)
        serializer = serializers.ProductSerializer(products, many=True)
        return Response(serializer.data)
