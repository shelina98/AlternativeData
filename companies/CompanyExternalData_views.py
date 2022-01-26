from googleapiclient.discovery import build
from rest_framework.decorators import api_view

from companies.models import CompanyExternalData, Company
from companies.serializers.serializer import CompanyExternalDataSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response

my_api_key = "AIzaSyBl8DTGupdA73zdLDs9hZbbCJk2Or28P6Y"
my_cse_id = "ea9823706ac6eff0f"

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



def google_search(search_term, api_key, cse_id, **kwargs):
    service = build("customsearch", "v1", developerKey=api_key)
    res = service.cse().list(q=search_term, cx=cse_id, **kwargs).execute()
    return res['items']


@api_view(['GET'])
def perform_google_search(request):
    company_name: object = request.query_params.get('name')
    results = google_search(company_name, my_api_key, my_cse_id, num=10)
    company = Company.objects.filter(name__icontains=company_name).first()

    for result in results:
        CompanyExternalData.objects.create(company=company,
                                           source=result['link'],
                                           title=result['title']).save()
    return Response('Search successfully happened!')


class CompanyExternalDataViewSet(ModelViewSet):
    queryset = CompanyExternalData.objects.all()
