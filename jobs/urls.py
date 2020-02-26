from django.urls import include, path
from rest_framework import routers
from jobs import views

router = routers.DefaultRouter()
router.register(r'categories', views.CategoryViewSet)

from . import views

urlpatterns = [
    path('', include(router.urls)),
]