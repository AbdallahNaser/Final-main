# Generated by Django 4.2.5 on 2024-01-30 20:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('RMS', '0024_rename_describtion_job_salray_remove_job_salay'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='job',
            name='other',
        ),
    ]