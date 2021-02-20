from django.http import HttpResponse
from django.shortcuts import render

from .models import User
import templates

import random as rd


'''
 Views
'''
def magiclink_view(request, *args, **kwargs):
    return render(request, "passless.html", {})


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