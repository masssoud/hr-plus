from jobs.models import Category
from rest_framework import viewsets
from jobs.serializers import CategoryListSerializer, CategoryDetailSerializer
from rest_framework import permissions
from rest_framework.decorators import action
from rest_framework.response import Response


class CategoryViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows categories to be viewed or edited.
    """
    queryset = Category.objects.all().order_by('title')
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_serializer_class(self):
        if self.action == 'list':
            return CategoryListSerializer
        else:
            return CategoryDetailSerializer

    @action(detail=False, methods=['get'])
    def all(self, request):
        serializer = CategoryListSerializer(self.queryset, many=True, context={'request': request})
        return Response(serializer.data)
