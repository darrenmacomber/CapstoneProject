# Generated by Django 2.2 on 2019-05-09 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('APILibraryApp', '0006_auto_20190507_1023'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='isbn',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='book',
            name='publish_date',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='book',
            name='publisher',
            field=models.CharField(max_length=200),
        ),
    ]