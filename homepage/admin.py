from django.contrib import admin
from . import models
# Register your models here.

admin.site.register(models.Topic)
admin.site.register(models.Comment)
admin.site.register(models.User)
admin.site.register(models.Picturewall)
admin.site.register(models.Funding)
admin.site.register(models.Job)
admin.site.register(models.GroupComment)
admin.site.register(models.GroupMessage)
admin.site.register(models.GroupRealation)
admin.site.register(models.Group)
