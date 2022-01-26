from django.contrib import admin

# Register your models here.

from .models import Company, CompanyExternalData

admin.site.register(Company)
admin.site.register(CompanyExternalData)
