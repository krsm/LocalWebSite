from django.db import models

# Create your models here.


class User(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    address_street = models.CharField(max_length=100)
    address_complement = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    email = models.CharField(unique=True)

    # TODO verify how to hash passwords using django