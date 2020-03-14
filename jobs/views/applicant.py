from jobs.models import Applicant, ApplicantHistory
from jobs.serializers import ApplicantListSerializer, ApplicantDetailSerializer, ApplicantHistorySerializer
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.decorators import action
from rest_framework.response import Response


class ApplicantViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows applicants to be viewed or edited.
    """
    queryset = Applicant.objects.all().order_by('-created_at')

    def get_queryset(self):
        """
        Optionally restricts the returned applicants to a given job posting,
        by filtering against some query parameters in the URL.
        """
        queryset = self.queryset
        job_posting = self.request.query_params.get('job_posting', None)
        status = self.request.query_params.get('status', None)
        full_name = self.request.query_params.get('full_name', None)
        if job_posting is not None:
            queryset = queryset.filter(job_posting=job_posting)
        if status is not None:
            queryset = queryset.filter(status=status)
        if full_name is not None:
            queryset = queryset.filter(full_name__icontains=full_name)
        return queryset

    def get_serializer_class(self):
        if self.action == 'list':
            return ApplicantListSerializer
        else:
            return ApplicantDetailSerializer

    def get_permissions(self):
        """
        Instantiates and returns the list of permissions that this view requires.
        """
        if self.action == 'create':
            permission_classes = []
        else:
            permission_classes = [permissions.IsAuthenticated]
        return [permission() for permission in permission_classes]

    @action(detail=True, methods=['get'])
    def history(self, request, pk=None):
        applicant = self.get_object()
        history = ApplicantHistory.objects.filter(applicant__pk=applicant.id).order_by('-created_at')
        serializer = ApplicantHistorySerializer(history, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['get'])
    def statuses(self, request, pk=None):
        statuses = {}
        for (choice, label) in Applicant.ApplicantStatus.choices:
            statuses[choice] = label
        return Response(statuses)
