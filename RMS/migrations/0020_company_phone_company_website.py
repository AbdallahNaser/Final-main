# Generated by Django 4.2.5 on 2024-01-29 22:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RMS', '0019_company_companytype_company_describtion'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='phone',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='company',
            name='website',
            field=models.CharField(max_length=100, null=True),
        ),
    ]