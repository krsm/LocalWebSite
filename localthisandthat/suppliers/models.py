from django.db import models

# Create your models here.

# TODO create relationship one to many with supplier and products


def upload_location(instance, filename):
    return "%s/%s" % (instance.supplier.id, filename)


class Supplier(models.Model):

    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=160, blank=True)
    zip = models.CharField(max_length=6)
    state = models.CharField(max_length=2)
    city = models.CharField(max_length=30)
    address_1 = models.CharField(max_length=50)
    address_2 = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        db_table = 'suppliers'
        ordering = ('updated_at',)
        verbose_name_plural = 'Suppliers'

    def __str__(self):
        return self.first_name


class Payment(models.Model):

    supplier = models.ForeignKey(
        Supplier,
        on_delete=models.CASCADE,
        # primary_key=True,
    )

    description = models.TextField(blank=True)
    value_payment = models.DecimalField(max_digits=6, decimal_places=2)
    payment_date = models.DateTimeField(auto_now=True)
    # TODO add field to upload file related to payment
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Product(models.Model):

    supplier = models.ForeignKey(
        Supplier,
        on_delete=models.CASCADE,
        # primary_key=True,
    )

    name = models.CharField(max_length=30)
    description = models.CharField(max_length=30)
    image = models.ImageField(upload_to=upload_location, blank=True)
    # received_qty =
    # delivered_qty =
    qty_weight = models.CharField(max_length=30)
    qty_units = models.CharField(max_length=30)
    price_per_weight = models.DecimalField(max_digits=6, decimal_places=2)
    price_per_unit = models.DecimalField(max_digits=6, decimal_places=2)
    category = models.CharField(max_length=30)
    received_at = models.DateTimeField()
    is_available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'products'
        ordering = ('updated_at',)
        verbose_name_plural = 'Products'

    def __str__(self):
        return self.name




    # fields related to delivery

#
# class Delivery(models.Model):
#
#     product = models.ForeignKey(
#         Supplier,
#         on_delete=models.CASCADE,
#         # primary_key=True,
#     )
#
#
    # TODO create class to associate qty delivered to a certain user and date

    # user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1)
    # title = models.CharField(max_length=120)
    # slug = models.SlugField(unique=True)
    # image = models.ImageField(upload_to=upload_location,
    #                           null=True,
    #                           blank=True,
    #                           width_field="width_field",
    #                           height_field="height_field")
    # height_field = models.IntegerField(default=0)
    # width_field = models.IntegerField(default=0)
    # content = models.TextField()
    # timestamp = models.DateTimeField(auto_now=True)
    # updated = models.DateTimeField(auto_now_add=True)