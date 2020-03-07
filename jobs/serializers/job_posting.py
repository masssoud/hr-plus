from jobs.models import JobPosting
from rest_framework import serializers


class JobPostingDetailSerializer(serializers.ModelSerializer):
    category_title = serializers.ReadOnlyField(source='category.title')
    class Meta:
        model = JobPosting
        fields = '__all__'
        read_only_fields = ['created_at', 'updated_at']


class JobPostingListSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobPosting
        fields = ['id', 'title', 'created_at', 'updated_at', 'url']
        read_only_fields = ['created_at', 'updated_at']
