from django.shortcuts import render
from django.http import	HttpResponse

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
	form = RegisterForm() # initialize the form

	if request.method == "POST": 
		gen_token = generate_token()
		form = RegisterForm(request.POST)

		if User.objects.get(email=form.data['email']) is None:
			if form.is_valid():
				obj, created = User.objects.get_or_create(email=form.data['email'], token=gen_token)
				form = RegisterForm(request.POST)
		elif User.objects.get(email=form.data['email']) != None:
			# raise forms.ValidationError("This email already exists")
			print("Email already exists")
			form = RegisterForm(request.POST)
			

	context = {
		"form": form,
		"token": gen_token
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