import uuid
from django.contrib.auth.models import User
from django.db import models


# Create your models here.


class Company(models.Model):
    owner = models.ForeignKey('auth.User', related_name='companies', on_delete=models.CASCADE, default=1)
    name = models.CharField(max_length=200, null=False, blank=False)
    vat = models.CharField(max_length=200, unique=True, editable=False, null=False, blank=False)
    country = models.CharField(max_length=200, blank=True, null=True)
    sector = models.CharField(max_length=200, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.name)

    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)


class CompanyExternalData(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE, null=True, blank=True)
    source = models.CharField(max_length=200, null=False, blank=False, unique=True)
    title = models.CharField(max_length=200, default='')
    country = models.CharField(max_length=200, null=True, blank=True)
    city = models.CharField(max_length=200, null=True, blank=True)
    address = models.CharField(max_length=200, null=True, blank=True)
    economy_sector = models.CharField(max_length=200, null=True, blank=True)
    website = models.CharField(max_length=500, null=True, blank=True)
    communication_information = models.CharField(max_length=200)
    founded = models.DateTimeField(null=True, blank=True)
    number_employees = models.IntegerField(default=0, null=True, blank=True)
    shareholders = models.IntegerField(default=0, null=True, blank=True)
    annual_gross_income = models.IntegerField(default=0, null=True, blank=True)
    datetime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
