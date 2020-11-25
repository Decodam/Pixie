# Generated by Django 3.1.3 on 2020-11-23 02:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Auth', '0004_profile_gender'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='story_pic',
        ),
        migrations.AlterField(
            model_name='profile',
            name='profile_pic',
            field=models.ImageField(blank=True, default='Avatar_4_kbds1n.png', upload_to='profile_pics'),
        ),
    ]