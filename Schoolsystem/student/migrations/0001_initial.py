# Generated by Django 3.2.5 on 2021-07-23 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=12)),
                ('last_name', models.CharField(max_length=12)),
                ('age', models.PositiveSmallIntegerField()),
                ('date_of_birth', models.DateField()),
                ('national_id', models.CharField(max_length=20)),
                ('guardian_name', models.CharField(max_length=12)),
                ('email_address', models.EmailField(max_length=254)),
                ('district', models.CharField(max_length=12)),
                ('medical_report', models.FileField(upload_to='')),
                ('date_of_enrollment', models.DateField()),
                ('laptop_number', models.CharField(max_length=10)),
            ],
        ),
    ]