from django.shortcuts import render
from django.http import HttpResponse

def index(request):
	return HttpResponse("Rango says hey there partner!<br/><a href='/rango/about/'>About</a>")

def about(request):
	return HttpResponse("Whats this all about, Rango?<br/><a href='/rango/'>Rango</a>")