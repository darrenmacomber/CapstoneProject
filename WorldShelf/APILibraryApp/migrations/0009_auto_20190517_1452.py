# Generated by Django 2.2 on 2019-05-17 21:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('APILibraryApp', '0008_auto_20190517_1203'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userbook',
            name='impressions',
        ),
        migrations.RemoveField(
            model_name='userbook',
            name='impressions_updated',
        ),
    ]
