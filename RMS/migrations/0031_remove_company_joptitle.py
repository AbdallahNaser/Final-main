# Generated by Django 4.2.5 on 2024-02-01 17:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('RMS', '0030_remove_job_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='company',
            name='joptitle',
        ),
    ]