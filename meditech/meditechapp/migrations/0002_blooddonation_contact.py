# Generated by Django 3.2 on 2021-04-24 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meditechapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blooddonation',
            name='contact',
            field=models.BigIntegerField(default=0),
        ),
    ]