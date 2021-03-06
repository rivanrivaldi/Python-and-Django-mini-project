# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-10-16 12:14
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('appointment', '0006_auto_20181014_1331'),
    ]

    operations = [
        migrations.CreateModel(
            name='Consultation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('consultation_number', models.CharField(max_length=250)),
                ('doctor_name', models.CharField(max_length=250)),
                ('patient_name', models.CharField(max_length=250)),
                ('file_number', models.CharField(max_length=20)),
                ('is_doctor', models.BooleanField(default=False)),
            ],
        ),
        migrations.AddField(
            model_name='appointment',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='consultation',
            name='appointment',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appointment.Appointment'),
        ),
    ]
