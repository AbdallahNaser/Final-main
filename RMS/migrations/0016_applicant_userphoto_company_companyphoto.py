# Generated by Django 4.2.5 on 2024-01-28 22:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RMS', '0015_applicant_user_company_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='applicant',
            name='userphoto',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='company',
            name='companyphoto',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]