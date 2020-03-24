from jobs.models import Comment
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework import status


class CommentSerializer(serializers.ModelSerializer):
    user_full_name = serializers.SerializerMethodField()

    def get_user_full_name(self, obj):
        if obj.user is None:
            return None
        full_name = '{} {}'.format(obj.user.first_name, obj.user.last_name)
        if full_name.strip() == '':
            full_name = obj.user.username
        return full_name.strip()

    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ['user', 'created_at', 'updated_at']
        extra_kwargs = {'applicant': {'write_only': True}}

    def create(self, validated_data):
        request = self.context.get("request")
        if request and hasattr(request, "user") and request.user.is_authenticated:
            validated_data['user'] = request.user
        comment = super(CommentSerializer, self).create(validated_data)
        return comment
