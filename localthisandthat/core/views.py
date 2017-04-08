from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


# Landing Page - Main Page
def home_page(request):

    return HttpResponse("<h1>Teste</h1>")