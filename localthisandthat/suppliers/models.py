from django.db import models

# Create your models here.

# TODO create relationship one to many with supplier and products


def upload_location(instance, filename):
    return "%s/%s" % (instance.supplier.id, filename)


class Supplier(models.Model):

    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=160)
    zip = models.CharField(max_length=6)
    state = models.CharField(max_length=2)
    city = models.CharField(max_length=30)
    address_1 = models.CharField(max_length=50)
    address_2 = models.CharField(max_length=50)
    timestamp = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField()
    is_active = models.BooleanField()

    class Meta:
        ordering = ('updated',)


class Payment(models.Model):
    pass
    # value to be pay
    # due to
    # last payment


class Product(models.Model):

    supplier = models.ForeignKey(
        Supplier,
        on_delete=models.CASCADE,
        # primary_key=True,
    )

    name = models.CharField(max_length=30)
    description = models.CharField(max_length=30)
    image = models.ImageField(upload_to=upload_location)
    # received_qty =
    # delivered_qty =
    weight = models.CharField(max_length=30)
    unit = models.CharField(max_length=30)
    price_weight = models.CharField(max_length=30)
    price_unit = models.CharField(max_length=30)
    category = models.CharField(max_length=30)
    timestamp = models.DateTimeField()
    updated = models.DateTimeField()


class Delivery(models.Model):
    pass
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