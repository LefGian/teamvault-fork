# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-21 14:11
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('auth', '0008_alter_user_username_max_length'),
        ('secrets', '0012_secret_search_index'),
    ]

    operations = [
        migrations.AddField(
            model_name='secret',
            name='owner_groups',
            field=models.ManyToManyField(blank=True, related_name='owned_passwords', to='auth.Group'),
        ),
        migrations.AddField(
            model_name='secret',
            name='owner_users',
            field=models.ManyToManyField(blank=True, related_name='owned_passwords', to=settings.AUTH_USER_MODEL),
        ),
    ]