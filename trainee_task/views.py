from django.shortcuts import render, get_object_or_404
from django.http import	HttpResponse
from django.core.mail import send_mail

from .models import User
from .forms import RegisterForm

import random as rd


'''
 Views
'''
def magiclink_view(request): # increment the value of counter by 1 and show the email/total
	rec_user_id = request.GET.get('email') # retrieve the user_id from the url
	rec_token = request.GET.get('token') # retrieve the token from the url

	obj = User.objects.get(email=rec_user_id, token=rec_token) # get the data related with a user
	obj.counter = increment(obj.counter)
	context = {
		'email': obj.email, 
		'counter': obj.counter 
	}

	obj.save()
	
	return render(request, "passless.html", context)


def register_view(request):
	gen_token = generate_token()
	initial_data = {
		'token': gen_token,
	}

	if request.method == "POST": 
		form = RegisterForm(request.POST, initial=initial_data)

		if form.is_valid():
			obj = User()
			obj.email = form.cleaned_data['email']
			obj.token = gen_token
			send_mail(
				'MagicLink to login to your account', # subject
				'Hello, here is a passwordless link: http://127.0.0.1:8000/?email={}&token={}'.format(form.cleaned_data['email'], gen_token), # message
				'tftptrainee@gmail.com', # from
				[form.cleaned_data['email']], # to
				)

			obj.save()
			form = RegisterForm()

		else:
			form = RegisterForm()
			

	context = {
		"form": form,
	}

	return render(request, "register.html", context)


''' 
 Methods
'''
def increment(base): 
	return base+1
def generate_token():
	random_hex = rd.randrange(10**80)
	hex = "%064x" % random_hex
	hex = hex[:16]
	return hex