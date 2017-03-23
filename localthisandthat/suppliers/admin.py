from django.contrib import admin

# Register your models here.
from .models import Supplier, Product


#
# # Registering the Post Model into admin site
# # and connects Post Model with PostModelAdmin
admin.site.register(Supplier)

admin.site.register(Product)
