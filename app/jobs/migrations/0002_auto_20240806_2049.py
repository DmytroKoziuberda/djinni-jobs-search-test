# Generated by Django 4.2.4 on 2024-08-06 20:49

from django.db import migrations
from django.contrib.postgres.operations import TrigramExtension


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0001_initial'),
    ]
    operations = [
        TrigramExtension(),
    ]