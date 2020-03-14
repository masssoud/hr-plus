from jobs.models import Comment
from jobs.serializers import CommentSerializer
from rest_framework import generics
from rest_framework import permissions


class CommentCreate(generics.CreateAPIView):
    """
    API endpoint that allows comments to created.
    """
    queryset = Comment.objects.all().order_by('-created_at')
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAdminUser]
