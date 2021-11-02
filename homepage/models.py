from django.db import models
import datetime
# Create your models here.
class User(models.Model):
    def __str__(self):
        return self.name
    name = models.CharField(max_length=30)
    password = models.CharField(max_length=20)
    avatar = models.ImageField(blank=True, null=True, upload_to='avatar/')
    email = models.EmailField()
    time_created = models.DateField(auto_now_add=True)
    is_superuser = models.BooleanField(auto_created=False)

class Topic(models.Model):
    def __str__(self):
        return self.title
    title = models.TextField(default="请输入你的标题")
    creator = models.CharField(max_length=30, default="xxx")
    content = models.TextField()
    cover_picture = models.ImageField(blank=True, null=True, upload_to='topic_pic/')
    time_created = models.DateField(auto_now_add=True)
    likes = models.IntegerField(default=0)
    is_vis = models.BooleanField()

class Comment(models.Model):
    creator = models.CharField(max_length=30, default="xxx")
    topic = models.CharField(max_length=50)
    content = models.TextField()
    time_created = models.DateField(auto_now_add=True)
    likes = models.IntegerField(default=0)
    is_vis = models.BooleanField()

class Picturewall(models.Model):
    picture = models.ImageField(blank=True, null=True, upload_to='topic_pic/')
    time_created = models.DateField(auto_now_add=True)

class Funding(models.Model):
    cover_pic = models.ImageField(blank=True, null=True, upload_to='topic_pic/')
    time_created = models.DateField(auto_now_add=True)
    creator = models.CharField(max_length=30, default="admin")
    title = models.CharField(max_length=100)
    need_money = models.IntegerField(default=0)
    have_money = models.IntegerField(default=0)

class Job(models.Model):
    def __str__(self):
        return self.title
    cover_pic = models.ImageField(blank=True, null=True, upload_to='topic_pic/')
    time_created = models.DateField(auto_now_add=True)
    creator = models.CharField(max_length=30, default="admin")
    title = models.CharField(max_length=100)
    pay_min = models.IntegerField()
    pay_max = models.IntegerField()
    related_label = models.CharField(max_length=100)
    where = models.CharField(max_length=100)
    discription = models.TextField()
    herf = models.CharField(max_length=1000, default="#")

class Group(models.Model):
    def __str__(self):
        return self.group_name
    group_name = models.CharField(max_length=100)
    user_number = models.IntegerField()
    cover_picture = models.ImageField(blank=True, null=True, upload_to='topic_pic/')
    is_lecture_group = models.BooleanField(default=False)
    about = models.TextField()
    is_vis = models.BooleanField(default=True)
    time_created = models.DateField(auto_now_add=True)

class GroupMessage(models.Model):
    def __str__(self):
        return self.title + "-" + self.group_name
    group_name = models.CharField(max_length=100, default="xxx")
    title = models.TextField(default="请输入你的标题")
    creator = models.CharField(max_length=30, default="xxx")
    content = models.TextField()
    cover_picture = models.ImageField(blank=True, null=True, upload_to='topic_pic/')
    time_created = models.DateField(auto_now_add=True)
    is_vis = models.BooleanField(default=True)

class GroupComment(models.Model):
    creator = models.CharField(max_length=30, default="xxx")
    topic = models.CharField(max_length=50)
    content = models.TextField()
    time_created = models.DateField(auto_now_add=True)
    likes = models.IntegerField(default=0)
    is_vis = models.BooleanField()

class GroupRealation(models.Model):
    group_name = models.CharField(max_length=100)
    user = models.CharField(max_length=100)

