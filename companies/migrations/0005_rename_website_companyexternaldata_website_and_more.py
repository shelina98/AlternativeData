# Generated by Django 4.0.1 on 2022-01-26 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0004_alter_companyexternaldata_website_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='companyexternaldata',
            old_name='Website',
            new_name='website',
        ),
        migrations.AlterField(
            model_name='companyexternaldata',
            name='source',
            field=models.CharField(max_length=200, unique=True),
        ),
    ]