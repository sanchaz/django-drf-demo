# Generated by Django 2.2.4 on 2019-08-03 23:51

from django.db import migrations

from django.contrib.auth.models import User
from ..models import DemoModel


def start_demo(apps, schema_editor):
    user = User.objects.create_superuser(username='demo', email='demo@demo.com', password='demo')
    DemoModel(user=user, field1="thisone", field2=True).save()


class Migration(migrations.Migration):

    dependencies = [
        ('demoapi', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(start_demo),
    ]
