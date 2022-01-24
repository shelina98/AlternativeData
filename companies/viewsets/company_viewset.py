from rest_framework import viewsets
from companies.models import Company
from companies.serializers.serializer import CompanySerializer


class CompanyViewSet(viewsets.ModelViewSet):
    """
        list, create, retrieve, update and destroy are automatically provided
    """
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
