# Generated by Django 3.1.3 on 2020-11-25 03:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Auth', '0015_remove_profile_notifications'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='show_email_to_public',
            field=models.BooleanField(default=False),
        ),
    ]