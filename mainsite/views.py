# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.

from django.template.loader import get_template
from django.http import HttpResponse
from mainsite import models


def index(request):
	template=get_template('index.html')
	posts=models.Post.objects.filter(enabled=True).order_by('-pub_time')[:30]
	moods=models.Mood.objects.all()	
	try:
		user_id=request.GET('user_id')
		user_pass=request.GET('user_pass')
		user_post=request.GET('user_post')
		user_mood=request.GET('mood')
	except:
		user_id=None
		message='如果要张贴信息，那么每一个字段都要填'
	if user_id!=None:
		mood=models.Mood.objects.get(status=user_mood)
		post=models.Post.objects.create(mood=mood,nickname=user_id,del_pass=user_pass,message=user_post)
		post.save()
		message='成功存储！请记得您的编辑密码[{}]！，信息须经审查后才会显示。'.format(user_pass)
	html=template.render(locals())
	return HttpResponse(html)
