# Generated by Django 3.1.5 on 2021-02-15 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poll', '0002_choice'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='question',
            name='tags',
            field=models.ManyToManyField(to='poll.Tag'),
        ),
    ]
