# Generated by Django 3.1.5 on 2021-01-25 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bike', '0003_auto_20210125_1411'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bike',
            name='device_id',
            field=models.IntegerField(unique=True),
        ),
    ]