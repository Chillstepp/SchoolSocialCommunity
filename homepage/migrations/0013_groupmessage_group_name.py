# Generated by Django 3.1 on 2021-11-01 05:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0012_group_time_created'),
    ]

    operations = [
        migrations.AddField(
            model_name='groupmessage',
            name='group_name',
            field=models.CharField(default='xxx', max_length=100),
        ),
    ]