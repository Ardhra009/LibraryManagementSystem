from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def welcome_Response(request):
    return HttpResponse("Welcome to Library Management")
def Library_Information(request):
    return HttpResponse("Welcome to Our Library")
def Book_List(request):
    return HttpResponse("Available Books: Python, Django, Java, React, MySQL")
def Book_Details(request):
    return HttpResponse("Book Name: Django | Author: William S. Vincent")
def Contact_Information(request):
    return HttpResponse("Contact us at library@gmail.com")