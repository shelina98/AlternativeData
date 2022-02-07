from django.contrib.auth.models import User
from rest_framework import serializers
from companies.models import Company, CompanyExternalData


class UserSerializer(serializers.ModelSerializer):
    companies = serializers.PrimaryKeyRelatedField(many=True, queryset=Company.objects.all())
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = User
        fields = ['id', 'username', 'companies', 'owner']


class CompanyUploadSerializer(serializers.Serializer):
    companyfile = serializers.FileField()


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ['name', 'vat', 'sector', 'country', 'id', 'owner']
        read_only_fields = ['created', 'id']


class CompanyExternalDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyExternalData
        fields = '__all__'
        read_only_fields = ['datetime', 'id']
