from rest_framework.decorators import api_view
from rest_framework import viewsets

from companies.models import CompanyExternalData
from companies.serializers.serializer import CompanyExternalDataSerializer
from rest_framework.response import Response


@api_view(['GET'])
def companyExternalDataList(request):
    companiesExternalData = CompanyExternalData.objects.all()
    serializer = CompanyExternalDataSerializer(companiesExternalData, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def singleCompanyExternalData(request, pk):
    CompanyExternalDataObj = CompanyExternalData.objects.get(id=pk)
    serializer = CompanyExternalDataSerializer(CompanyExternalDataObj)
    return Response(serializer.data)


class CompanyExternalDataViewSet(viewsets.ModelViewSet):
    queryset = CompanyExternalData.objects.all()
    serializer_class = CompanyExternalDataSerializer
