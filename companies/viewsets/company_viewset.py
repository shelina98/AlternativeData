from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
import requests
from companies.models import Company
from companies.serializers.serializer import CompanySerializer
from companies.services.googleservices import GoogleService
from companies.services.aggregate_services import AggregateService

from django_filters.rest_framework import DjangoFilterBackend
from companies.filtersets.filterset import CompanyFilter


class CompanyViewSet(viewsets.ModelViewSet):
    """
        list, create, retrieve, update and destroy are automatically provided
    """
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = CompanyFilter
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    @action(detail=True, methods=['GET'])
    def perform_google_search(self, request, pk=None):
        # company = Company.objects.get(id=pk)
        company = self.get_object()
        results = GoogleService.google_search(search_term=company.name, num=10)
        GoogleService.process_results(results=results, company=company)
        return Response('Search successfully happened!')

    @action(detail=False, methods=['GET'])
    def call_phantom_agent(self, request, pk=None):
        pass

    @action(detail=True, methods=['GET'])
    def get_external_data(self, request, pk=None):
        company = self.get_object()
        results = GoogleService.external(company=company)
        return Response(results.data)

    @action(detail=False, methods=['GET'])
    def numberOfcompanies(self, request):
        companies = Company.objects.all()
        results = AggregateService.numberOfcompanies(companies=companies)
        return Response(results)

    @action(detail=False, methods=['GET'])
    def numberOfcompaniesCountry(self, request):
        companies = Company.objects.all()
        results = AggregateService.numberOfcompaniesCountry(companies=companies)
        return Response(results)

    @action(detail=False, methods=['GET'])
    def numberOfcompaniesSector(self, request):
        companies = Company.objects.all()
        results = AggregateService.numberOfcompaniesSector(companies=companies)
        return Response(results)
