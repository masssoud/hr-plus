from django.urls import include, path
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns
from jobs import views

router = routers.DefaultRouter()
router.register(r'categories', views.CategoryViewSet)
router.register(r'job-postings', views.JobPostingViewSet)
router.register(r'applicants', views.ApplicantViewSet)

from . import views

urlpatterns = [
    path('comments/', views.CommentCreate.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns) + [path('', include(router.urls))]