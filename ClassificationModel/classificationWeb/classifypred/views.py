from django.shortcuts import render
from django.http import HttpResponse
from classifypred.forms import *
# Create your views here.

def testHealth(request):
    return HttpResponse("<h1>working</h1>")

def testPage(request):
    return render(request,"Home.html",{"var1":"This works!","age":18})

def showDocs(request):
    pass


def login(request):
    username="not logged in"
    if request.method=="POST":
        MyLoginForm=LoginForm(request.POST)
        if MyLoginForm.is_valid():
            print("Valid")
            username=MyLoginForm.cleaned_data['username']
        else:
            print("Invalid")
    else:
        MyLoginForm=LoginForm()
    return render(request,"after_login.html",{"username":username})