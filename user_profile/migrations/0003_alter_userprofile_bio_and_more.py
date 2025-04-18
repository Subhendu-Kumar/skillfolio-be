# Generated by Django 5.2 on 2025-04-06 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0002_userprofile_is_complete'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='bio',
            field=models.TextField(blank=True, default='demo demo'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='current_position',
            field=models.CharField(blank=True, default='example', max_length=255),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='experience_years',
            field=models.DecimalField(blank=True, decimal_places=1, default=4.5, max_digits=4),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='full_name',
            field=models.CharField(blank=True, default='demo name', max_length=255),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='github',
            field=models.URLField(blank=True, default='https://example.com'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='graduation_year',
            field=models.PositiveIntegerField(blank=True, default=2004),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='highest_qualification',
            field=models.CharField(blank=True, default='example', max_length=255),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='linkedin',
            field=models.URLField(blank=True, default='https://example.com'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='location',
            field=models.CharField(blank=True, default='india', max_length=255),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='phone_number',
            field=models.CharField(blank=True, default='1230987654', max_length=20),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='portfolio',
            field=models.URLField(blank=True, default='https://example.com'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='skills',
            field=models.TextField(blank=True, default='example, demo', help_text='Comma-separated skills (e.g. Python, Django, React)'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='university',
            field=models.CharField(blank=True, default='example', max_length=255),
        ),
    ]
