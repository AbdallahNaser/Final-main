# Generated by Django 4.2.5 on 2024-02-04 23:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RMS', '0041_remove_applicant_department_department_applicants_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='companyphoto',
            field=models.ImageField(blank=True, default='company.png', null=True, upload_to=''),
        ),
    ]