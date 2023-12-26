# Generated by Django 5.0 on 2023-12-20 18:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('School_App', '0006_teachers_info_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClassInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('className', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('studentName', models.CharField(default='', max_length=50)),
                ('studentId', models.CharField(default='', max_length=50)),
                ('fatherName', models.CharField(default='', max_length=50)),
                ('motherName', models.CharField(default='', max_length=50)),
                ('habitation', models.CharField(default='', max_length=50)),
                ('aadharUidNo', models.CharField(default='', max_length=50)),
                ('doa', models.DateField(blank=True, null=True)),
                ('dob', models.DateField(blank=True, null=True)),
                ('sex', models.CharField(default='', max_length=50)),
                ('caste', models.CharField(default='', max_length=50)),
                ('subCaste', models.CharField(default='', max_length=50)),
                ('minority', models.CharField(default='', max_length=50)),
                ('bplNo', models.CharField(default='', max_length=50)),
                ('disadvantageBhagyalakshmiBondNo', models.CharField(default='', max_length=50)),
                ('adminRte', models.CharField(default='', max_length=50)),
                ('classStudying', models.CharField(default='', max_length=50)),
                ('previousClass', models.CharField(default='', max_length=50)),
                ('statusIf', models.CharField(default='', max_length=50)),
                ('medium', models.CharField(default='', max_length=50)),
                ('syllabus', models.CharField(default='', max_length=50)),
                ('disability', models.CharField(default='', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='TeachersInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('academicYear', models.CharField(default='', max_length=50)),
                ('stsTeacherId', models.CharField(default='', max_length=50)),
                ('kgId', models.CharField(default='', max_length=50)),
                ('name', models.CharField(default='', max_length=50)),
                ('dob', models.DateField(blank=True, null=True)),
                ('gender', models.CharField(default='', max_length=50)),
                ('mobileNo', models.CharField(default='', max_length=50)),
                ('status', models.CharField(default='', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='StudentClass',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('classInfo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='School_App.classinfo')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='School_App.student')),
            ],
        ),
    ]
