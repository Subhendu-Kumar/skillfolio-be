# Generated by Django 5.2 on 2025-04-06 18:17

import django.db.models.deletion
import uuid
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Statistics',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('jobs_visited', models.IntegerField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='statistics', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'statistics',
                'verbose_name_plural': 'statistics',
                'db_table': 'statistics',
            },
        ),
    ]
