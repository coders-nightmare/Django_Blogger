from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def blogHome(request):
    return HttpResponse("<h1>Welcome to Blog</h1>")


def blogPost(request, slug):
    return HttpResponse(f"<h1>Welcome to Blog {slug} </h1>")
