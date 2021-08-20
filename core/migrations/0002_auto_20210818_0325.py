# Generated by Django 3.0.8 on 2021-08-18 03:25

import core.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='banner',
            field=models.ImageField(blank=True, upload_to=core.models.user_directory_path_banner),
        ),
        migrations.AlterField(
            model_name='profile',
            name='picture',
            field=models.ImageField(blank=True, upload_to=core.models.user_directory_path_profile),
        ),
        migrations.AlterField(
            model_name='profile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL),
        ),
    ]