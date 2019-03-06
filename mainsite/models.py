# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Mood(models.Model):
	status=models.CharField(max_length=10,null=False)
	def __unicode__(self):
		return self.status
		
class Post(models.Model):
	#定义多对一关系，一种心情可以对应多个用户，但一个用户只能有一种心情。删除心情时，引用这种心情的用户也要被删除。
	mood=models.ForeignKey('Mood', on_delete=models.CASCADE)
	nickname=models.CharField(max_length=10,default='不愿意透露身份的人')
	message=models.TextField(null=False)
	del_pass=models.CharField(max_length=10)
	pub_time=models.DateTimeField(auto_now=True)
	enabled=models.BooleanField(default=False)
	def __unicode__(self):
		return self.message