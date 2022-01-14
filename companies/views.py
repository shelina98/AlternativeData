from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.viewsets import ModelViewSet
from .serializer import CompanySerializer

# Create your views here.

from .models import Company


def Companies(request):
    Companies = Company.objects.all()
    context = {'Companies': Companies}
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


class CompanyViewSet(ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
