from django.contrib import admin

# Register your models here.
from .models import Supplier, Product


#
# # Registering the Post Model into admin site
# # and connects Post Model with PostModelAdmin
# admin.site.register(Supplier)
#
# admin.site.register(Product)

# create class to customize admin
class SuppliersModelAdmin(admin.ModelAdmin):
    list_display = ["first_name", "last_name", "email", "is_active"]
    list_display_link = ["created_at"]
    list_filter = ["created_at", "updated_at"]
    # list_editable = ["is_active"]
    search_fields = ["first_name", "is_active"]

    class Meta:
        model = Supplier
        # first_name
        # last_name
        # email
        # zip
        # state
        # city
        # address_1
        # address_2
        # created_at
        # updated_at
        # is_active


class ProductsModelAdmin(admin.ModelAdmin):

        list_display = ["name", "qty_weight", "qty_units", "price_per_weight", "price_per_unit"]
        list_display_link = ["created_at"]
        list_filter = ["created_at", "received_at"]
        # list_editable = ["is_active"]
        search_fields = ["name", "category"]

        class Meta:
            model = Product


                # name = models.CharField(max_length=30)
                # description = models.CharField(max_length=30)
                # image = models.ImageField(upload_to=upload_location, blank=True)
                # # received_qty =
                # # delivered_qty =
                # qty_weight = models.CharField(max_length=30)
                # qty_units = models.CharField(max_length=30)
                # price_per_weight = models.DecimalField(max_digits=6, decimal_places=2)
                # price_per_unit = models.DecimalField(max_digits=6, decimal_places=2)
                # category = models.CharField(max_length=30)
                # received_at = models.DateTimeField()
                # created_at = models.DateTimeField(auto_now_add=True)
                # updated_at = models.DateTimeField(auto_now=True)


# Registering the Post Model into admin site
# and connects Post Model with PostModelAdmin
admin.site.register(Supplier, SuppliersModelAdmin)
admin.site.register(Product, ProductsModelAdmin)