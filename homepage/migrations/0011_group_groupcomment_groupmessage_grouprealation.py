# Generated by Django 3.1 on 2021-10-31 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0010_job_herf'),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group_name', models.CharField(max_length=100)),
                ('user_number', models.IntegerField()),
                ('cover_picture', models.ImageField(blank=True, null=True, upload_to='topic_pic/')),
                ('is_lecture_group', models.BooleanField(default=False)),
                ('about', models.TextField()),
                ('is_vis', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='GroupComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creator', models.CharField(default='xxx', max_length=30)),
                ('topic', models.CharField(max_length=50)),
                ('content', models.TextField()),
                ('time_created', models.DateField(auto_now_add=True)),
                ('likes', models.IntegerField(default=0)),
                ('is_vis', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='GroupMessage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(default='请输入你的标题')),
                ('creator', models.CharField(default='xxx', max_length=30)),
                ('content', models.TextField()),
                ('cover_picture', models.ImageField(blank=True, null=True, upload_to='topic_pic/')),
                ('time_created', models.DateField(auto_now_add=True)),
                ('is_vis', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='GroupRealation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group_name', models.CharField(max_length=100)),
                ('user', models.CharField(max_length=100)),
            ],
        ),
    ]