from django.shortcuts import render
from django.http import HttpResponse
# import models related to suppliers app
# to be used to display info related products
from ..suppliers.models import Product

# Create your views here.
# Landing Page - Main Page
def home_page(request):
    test_html = {'test': 'test'}
    return render(request, 'main_page.html', test_html)
