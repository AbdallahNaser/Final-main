# Generated by Django 4.2.7 on 2024-04-02 13:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('RMS', '0053_alter_applicant_birthdate'),
    ]

    operations = [
        migrations.CreateModel(
            name='jobstatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('percentage', models.FloatField(default=0)),
                ('applicant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='RMS.applicant')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='RMS.company')),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='RMS.job')),
            ],
        ),
    ]