# Generated by Django 4.2.5 on 2024-02-02 03:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('RMS', '0035_alter_education_applicant_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='certificate',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('place', models.CharField(max_length=1000, null=True)),
                ('major', models.CharField(max_length=1000, null=True)),
                ('about', models.CharField(max_length=1000, null=True)),
                ('applicant', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='RMS.applicant')),
            ],
        ),
    ]
