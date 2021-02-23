from django import forms

from .models import User


class RegisterForm(forms.Form):
	email	= forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Your Email'}))
	token	= forms.HiddenInput()

	# class Meta: 
	# 	model = User
	# 	fields = ('email', 'token')	
