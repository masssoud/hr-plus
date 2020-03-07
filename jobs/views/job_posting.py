from jobs.models import JobPosting
from rest_framework import viewsets
from jobs.serializers import JobPostingListSerializer, JobPostingDetailSerializer
from rest_framework import permissions


class JobPostingViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows categories to be viewed or edited.
    """
    queryset = JobPosting.objects.all().order_by('title')
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_serializer_class(self):
        if self.action == 'list':
            return JobPostingListSerializer
        else:
            return JobPostingDetailSerializer
