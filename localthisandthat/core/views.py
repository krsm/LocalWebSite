
from django.apps import apps


from django.shortcuts import render
from django.http import HttpResponse
# import models related to suppliers app
# to be used to display info related products
# from ..suppliers.models import Product


# Create your views here.
# Landing Page - Main Page
def home_page(request):
    # getting the Products Model
    products_model = apps.get_model('suppliers', 'Product')
    products = products_model.objects.all().order_by('-id')
    # print(products)
    test_html = {'products': products}
    return render(request, 'core/main_page.html', test_html)
