# Generated by Django 3.1.3 on 2020-11-23 03:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Auth', '0009_auto_20201123_0850'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='story_pics',
            field=models.ImageField(default='default_story_upkhp7.jpg', upload_to='story_pics'),
        ),
        migrations.DeleteModel(
            name='Story',
        ),
    ]
