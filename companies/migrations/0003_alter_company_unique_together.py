# Generated by Django 4.0.1 on 2022-01-17 10:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0002_remove_company_vat_company_vat'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='company',
            unique_together={('name', 'id')},
        ),
    ]
