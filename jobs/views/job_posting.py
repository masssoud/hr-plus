from jobs.models import JobPosting
from rest_framework import viewsets
from jobs.serializers import JobPostingListSerializer, JobPostingDetailSerializer
from rest_framework import permissions
from rest_framework.decorators import action
from rest_framework.response import Response


class JobPostingViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows categories to be viewed or edited.
    """
    queryset = JobPosting.objects.all().order_by('title')
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        """
        Optionally restricts the returned job_posting to a given job posting,
        by filtering against some query parameters in the URL.
        """
        queryset = self.queryset
        category = self.request.query_params.get('category', None)
        is_open = self.request.query_params.get('is_open', None)
        if category is not None:
            queryset = queryset.filter(category=category)
        if is_open is not None:
            queryset = queryset.filter(is_open=(int(is_open)==1))
        return queryset

    def get_serializer_class(self):
        if self.action == 'list':
            return JobPostingListSerializer
        else:
            return JobPostingDetailSerializer

    @action(detail=False, methods=['get'])
    def all(self, request):
        serializer = JobPostingListSerializer(self.queryset, many=True, context={'request': request})
        return Response(serializer.data)
