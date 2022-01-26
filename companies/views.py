from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.viewsets import ModelViewSet
from companies.serializers.serializer import CompanySerializer, CompanyUploadSerializer
from rest_framework import generics, status
import pandas as pd
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
# Create your views here.
from companies.models import Company


def Companies(request):
    Companies = Company.objects.all()
    number = Companies.count()
    context = {'Companies': Companies, 'number': number}
    return render(request, 'companies/companies.html', context)


@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'List': '/task-list/',
        'Detail View': '/task-detail/<str:pk>/',
        'Create': '/task-create/',
    }
    return Response(api_urls)


@api_view(['GET'])
def companyList(request):
    companies = Company.objects.all()
    serializer = CompanySerializer(companies, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def singleCompany(request, pk):
    CompanyObj = Company.objects.get(id=pk)
    serializer = CompanySerializer(CompanyObj)
    return Response(serializer.data)


@api_view(['POST'])
def companyCreate(request):
    serializer = CompanySerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['POST'])
def companyUpdate(request, pk):
    companyObj = Company.objects.get(id=pk)
    serializer = CompanySerializer(instance=companyObj, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['DELETE'])
def companyDelete(request, pk):
    companyObj = Company.objects.get(id=pk)
    companyObj.delete()
    return Response('Item successfully deleted!')


class CompanyViewSet(ModelViewSet):
    serializer_class = CompanySerializer
    queryset = Company.objects.all()


class UploadFileView(generics.CreateAPIView):
    serializer_class = CompanyUploadSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        companyfile = serializer.validated_data['companyfile']
        reader = pd.read_csv(companyfile)
        for _, row in reader.iterrows():
            new_company = Company(
                name=row["name"],
                vat=row['vat'],
                country=row["country"],
                sector=row["sector"]
            )
            new_company.save()
        return Response({"status": "success"}, status.HTTP_201_CREATED)
