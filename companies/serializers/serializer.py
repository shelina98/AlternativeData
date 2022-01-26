from rest_framework import serializers
from companies.models import Company, CompanyExternalData


class CompanyUploadSerializer(serializers.Serializer):
    companyfile = serializers.FileField()


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ['name', 'vat', 'sector', 'country', 'id']
        read_only_fields = ['created', 'id']


class CompanyExternalDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyExternalData
        fields = '__all__'
        read_only_fields = ['datetime', 'id']
