from django.shortcuts import render

#  from django.http import HttpResponse

# Create your views here.

def HomePage(request):
    return render(request, 'HomePage.html')

def contactPage(request):
    return render(request, 'contactPage.html')

def AboutPage(request):
    return render(request, 'AboutPage.html')
