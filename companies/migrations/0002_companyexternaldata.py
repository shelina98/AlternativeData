# Generated by Django 4.0.1 on 2022-01-24 14:22

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CompanyExternalData',
            fields=[
                ('source', models.CharField(max_length=200)),
                ('country', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=200)),
                ('economy_sector', models.CharField(max_length=200)),
                ('Website', models.CharField(max_length=500)),
                ('communication_information', models.CharField(max_length=200)),
                ('founded', models.DateTimeField(blank=True, null=True)),
                ('number_employees', models.IntegerField(blank=True, default=0, null=True)),
                ('shareholders', models.IntegerField(blank=True, default=0, null=True)),
                ('annual_gross_income', models.IntegerField(blank=True, default=0, null=True)),
                ('datetime', models.DateTimeField(auto_now_add=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('company', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='companies.company')),
            ],
        ),
    ]
