# Generated by Django 3.1.3 on 2020-11-24 08:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Posts', '0007_auto_20201124_0932'),
        ('Auth', '0013_auto_20201123_1341'),
    ]

    operations = [
        migrations.AddField(
            model_name='notification',
            name='post',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_who_is_the_target', to='Posts.post'),
        ),
    ]