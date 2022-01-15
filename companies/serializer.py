from rest_framework import serializers
from .models import Company


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ['name', 'VAT', 'sector', 'country']
        read_only_fields = ['id', 'created']
