from django.urls import include, path
from rest_framework import routers
from jobs import views

router = routers.DefaultRouter()
router.register(r'categories', views.CategoryViewSet)
router.register(r'job-postings', views.JobPostingViewSet)
router.register(r'applicants', views.ApplicantViewSet)

from . import views

urlpatterns = [
    path('', include(router.urls)),
]