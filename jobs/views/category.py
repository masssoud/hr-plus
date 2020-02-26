from jobs.models import Category
from rest_framework import viewsets
from jobs.serializers import CategorySerializer
from rest_framework import permissions


class CategoryViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows categories to be viewed or edited.
    """
    queryset = Category.objects.all().order_by('title')
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]