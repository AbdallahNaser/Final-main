# Generated by Django 4.2.5 on 2024-01-30 23:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RMS', '0026_remove_company_jobs_job_companies'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
