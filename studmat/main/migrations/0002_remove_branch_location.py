# Generated by Django 4.2.4 on 2023-08-25 19:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='branch',
            name='location',
        ),
    ]