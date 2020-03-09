from jobs.models import Applicant, ApplicantHistory, JobPosting
from rest_framework import serializers
from ..validators import validate_pdf
from django.core.validators import FileExtensionValidator


class ApplicantDetailSerializer(serializers.ModelSerializer):
    job_posting_title = serializers.ReadOnlyField(source='job_posting.title')
    cv = serializers.FileField(allow_empty_file=False,
                               validators=[validate_pdf, FileExtensionValidator(['pdf'])])
    job_posting = serializers.PrimaryKeyRelatedField(many=False, required=True, queryset=JobPosting.objects.all())

    class Meta:
        model = Applicant
        fields = '__all__'
        read_only_fields = ['created_at', 'updated_at']

    def create(self, validated_data):
        applicant = super(ApplicantDetailSerializer, self).create(validated_data)
        applicant_history = ApplicantHistory(
            status=applicant.status,
            applicant=applicant,
        )
        request = self.context.get("request")
        if request and hasattr(request, "user") and request.user.is_authenticated:
            applicant_history.user = request.user
        applicant_history.save()
        return applicant

    def update(self, instance, validated_data):
        old_status = instance.status
        applicant = super(ApplicantDetailSerializer, self).update(instance, validated_data)
        if 'status' in validated_data and old_status != validated_data['status']:
            applicant_history = ApplicantHistory(
                status=validated_data['status'],
                applicant=applicant,
            )
            request = self.context.get("request")
            if request and hasattr(request, "user") and request.user.is_authenticated:
                applicant_history.user = request.user
            applicant_history.save()
        return applicant


class ApplicantListSerializer(serializers.ModelSerializer):
    job_posting_title = serializers.ReadOnlyField(source='job_posting.title')

    class Meta:
        model = Applicant
        fields = ['id', 'full_name', 'job_posting_title', 'status', 'created_at', 'updated_at', 'url']
        read_only_fields = ['created_at', 'updated_at']


class ApplicantHistorySerializer(serializers.ModelSerializer):
    user_full_name = serializers.SerializerMethodField()

    def get_user_full_name(self, obj):
        if obj.user is None:
            return None
        full_name = '{} {}'.format(obj.user.first_name, obj.user.last_name)
        if full_name.strip() == '':
            full_name = obj.user.username
        return full_name.strip()

    class Meta:
        model = ApplicantHistory
        fields = '__all__'
        read_only_fields = ['created_at', 'updated_at']
