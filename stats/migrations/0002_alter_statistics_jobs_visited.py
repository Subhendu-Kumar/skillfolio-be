# Generated by Django 5.2 on 2025-04-06 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stats', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='statistics',
            name='jobs_visited',
            field=models.IntegerField(default=0),
        ),
    ]
