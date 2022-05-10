from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index (request):
    return render(request,'index.html')

def login (request):
    return render (request , 'login.html')

def contactus(request):
    return HttpResponse("contact us page")

def about(request):
    return HttpResponse("ABOUT US")


