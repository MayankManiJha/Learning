from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def testHealth(response):
    return HttpResponse("<h1>working</h1>")

def showDocs(response):
    pass