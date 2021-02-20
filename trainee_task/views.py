from django.shortcuts import render

from .models import User
import random as rd


'''
 Views
'''
def magiclink_view(request): # increment the value of counter by 1 and show the email/total
	obj = User.objects.get(user_id=1)
	obj.counter = increment(obj.counter)
	context = {
		'email': obj.email, 
		'counter': obj.counter 
	}

	obj.save()
	
	return render(request, "passless.html", context)


''' 
 Methods
'''
def increment(base): 
	return base+1
def token():
	random_hex = rd.randrange(10**80)
	hex = "%064x" % random_hex
	hex = hex[:16]
	return hex