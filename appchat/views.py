from django.shortcuts import render
from django.http import HttpResponse

from django.views import generic

from django.utils.decorators import method_decorator

# Create your views here.

def testing(request):
	return HttpResponse("Testing successful...")


class CommonUrl(generic.View):

	def get(self, request, *args, **kwargs):
		return HttpResponse("Hello")


class ChatBot(generic.View):

	def get(self, request, *args, **kwargs):
		return HttpResponse("chat")