from django.shortcuts import render
from django.http import  HttpResponse

def index (request):
    return HttpResponse("Hellow World")
def contacts (request):
    return HttpResponse( 'blog/post_list.html', {})