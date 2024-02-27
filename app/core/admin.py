from django.contrib import admin
from . import models
# Register your models here.


admin.site.register(models.User)
admin.site.register(models.Task)
admin.site.register(models.Schedule)
admin.site.register(models.Assignment)
admin.site.register(models.Notification)