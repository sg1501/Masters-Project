# Generated by Django 2.0 on 2019-08-14 15:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0005_appointment_stats'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appointment',
            name='stats',
        ),
        migrations.RemoveField(
            model_name='doctor',
            name='stats',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='stats',
        ),
    ]
