from django.shortcuts import render
from django.http import HttpResponse

def index(request):
	return  HttpResponse('<h1>Coming soon </h1><br>looking for<br>⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇<br> <a href="/questions/">click for questions</a>')
