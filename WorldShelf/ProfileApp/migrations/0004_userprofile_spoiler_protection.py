# Generated by Django 2.2 on 2019-05-20 21:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ProfileApp', '0003_auto_20190509_1445'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='spoiler_protection',
            field=models.BooleanField(default=False),
        ),
    ]
