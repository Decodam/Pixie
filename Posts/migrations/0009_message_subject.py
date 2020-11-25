# Generated by Django 3.1.3 on 2020-11-25 02:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Posts', '0008_message'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='subject',
            field=models.CharField(choices=[('Report-bugs', 'Report-bugs'), ('Report-posts', 'Report-posts'), ('Report-users', 'Report-users'), ('Help for projects', 'Help for projects'), ('For business', 'For business'), ('Others', 'Others')], max_length=200, null=True),
        ),
    ]
