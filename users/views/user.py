from django.contrib.auth.models import User
from rest_framework import viewsets
from users.serializers import UserListSerializer, UserDetailSerializer, CreateUpdateUserSerializer
from rest_framework import permissions
from rest_framework.decorators import action
from rest_framework.response import Response


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows categories to be viewed or edited.
    """
    queryset = User.objects.all().order_by('date_joined')
    permission_classes = [permissions.IsAdminUser]

    def get_serializer_class(self):
        if self.action == 'list':
            return UserListSerializer
        elif self.action == 'create' or self.action == 'update' or self.action == 'partial_update':
            return CreateUpdateUserSerializer
        elif self.action == 'current_user':
            return UserDetailSerializer
        else:
            return UserDetailSerializer

    @action(detail=False, methods=['get'], url_path='current-user', permission_classes=[permissions.IsAuthenticated])
    def current_user(self, request):
        user = request.user
        serializer = self.get_serializer(user, many=False)
        return Response(serializer.data)
