from django.shortcuts import render
from django.http import HttpResponse
def index(request):
    return HttpResponse("Hellow World")
def site(request):
    return render(request,"blog.html")