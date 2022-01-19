from rest_framework import serializers
from .models import Company


class CompanyUploadSerializer(serializers.Serializer):
    companyfile = serializers.FileField()


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ['name', 'vat', 'sector', 'country', 'id']
        read_only_fields = ['created','id']
