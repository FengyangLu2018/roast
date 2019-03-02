# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from mainsite import models
class PostAdmin(admin.ModelAdmin):
	list_display=('nickname','message','enabled','pub_time')
	ordering=('-pub_time',)
admin.site.register(models.Mood)
admin.site.register(models.Post,PostAdmin)
