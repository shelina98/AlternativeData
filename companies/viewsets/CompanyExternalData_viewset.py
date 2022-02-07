from rest_framework import viewsets, permissions
from companies.models import CompanyExternalData
from companies.serializers.serializer import CompanyExternalDataSerializer


class CompanyExternalDataViewSet(viewsets.ModelViewSet):
    queryset = CompanyExternalData.objects.all()
    serializer_class = CompanyExternalDataSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
