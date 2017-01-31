from django.shortcuts import render
from django.http import HttpResponse

from django.views import generic

from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

import requests
import json

# Create your views here.

def testing(request):
	return HttpResponse("Testing successful...")


class CommonUrl(generic.View):

	def get(self, request, *args, **kwargs):
		return HttpResponse("Hello")


class ChatBot(generic.View):

	def get(self, request, *args, **kwargs):
		print self.request.GET
		if self.request.GET.get('hub.verify_token') == '123456789':
			return HttpResponse(self.request.GET['hub.challenge'])
		else:
			return HttpResponse('Error, invalid token')

	@method_decorator(csrf_exempt)
	def dispatch(self, request, *args, **kwargs):
		return generic.View.dispatch(self, request, *args, **kwargs)

	def post(self, request, *args, **kwargs):
		print self.request.body
		return HttpResponse("None")