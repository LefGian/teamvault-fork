# Generated by Django 4.2.3 on 2023-07-11 18:56

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("accounts", "0002_add_user_settings"),
    ]

    operations = [
        migrations.AddField(
            model_name="usersettings",
            name="avatar",
            field=models.BinaryField(blank=True, null=True),
        ),
    ]