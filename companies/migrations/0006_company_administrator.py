# Generated by Django 4.0.1 on 2022-01-31 16:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('companies', '0005_rename_website_companyexternaldata_website_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='administrator',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='companies', to=settings.AUTH_USER_MODEL),
        ),
    ]
