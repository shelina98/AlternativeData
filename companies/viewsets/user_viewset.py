from rest_framework import viewsets, permissions
from django.contrib.auth.models import User
from rest_framework.decorators import action
from rest_framework.response import Response
from companies.serializers.serializer import UserSerializer
from companies.services.user_services import UserService


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    @action(detail=True, methods=['GET'])
    def get_companies(self, request, pk=None):
        user = self.get_object()
        results = UserService.get_companies(user=user)
        return Response(results.data)
