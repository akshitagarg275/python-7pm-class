from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def homePage(request):
    # return HttpResponse("<h1>Welcome to home page </h1>")
    return render(request, 'hola/homepage.html')

def contactPage(request):
    # return HttpResponse("<h1>Welcome to contact page </h1>")
    return render(request, 'hola/contactpage.html')

def aboutPage(request):
    # return HttpResponse("<h1>Welcome to about page </h1>")
    return render(request, 'hola/aboutpage.html')