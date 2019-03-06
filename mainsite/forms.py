# -*- coding: utf-8 -*-
from django import forms
from mainsite import models
from captcha.fields import CaptchaField

class ContactForm(forms.Form):
	CITY=[
		['TP','taipei'],
		['TY','taoyuan'],
		['TC','taichung'],
		['TN','tainan'],
		['KS','kaohsiung'],
		['NA','others'],
	]
	user_name=forms.CharField(label='您的姓名',max_length=50,initial='lidaren')
	user_city=forms.ChoiceField(label='居住城市',choices=CITY)
	user_school=forms.BooleanField(label='是否在学',required=False)
	user_email=forms.EmailField(label='电子邮件')
	user_message=forms.CharField(label='您的意见',widget=forms.Textarea)
	
class PostForm(forms.ModelForm):
	captcha=CaptchaField()
	class Meta:
		model=models.Post
		fields=['mood','nickname','message','del_pass']
	def __init__(self,*args,**kwargs):
		super(PostForm,self).__init__(*args,**kwargs)
		self.fields['mood'].label='现在的心情'
		self.fields['nickname'].label='您的昵称'
		self.fields['message'].label='心情留言'
		self.fields['del_pass'].label='设置密码'
		self.fields['captcha'].label='确定您不是机器人'