# Generated by Django 3.2.5 on 2021-08-12 20:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Courses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=12, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('course_duration', models.DurationField(blank=True, null=True)),
                ('course_code', models.CharField(blank=True, max_length=30, null=True)),
                ('schedule', models.FileField(blank=True, null=True, upload_to='')),
                ('syllabus', models.TextField(blank=True, null=True)),
                ('course_Time', models.TimeField(blank=True, null=True)),
                ('date_enrolled', models.DateField(blank=True, null=True)),
            ],
        ),
    ]
