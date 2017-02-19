from django.db import models
from django.contrib.auth.models import User
# Signals
from django.db.models.signals import post_save


#  Extending User Model Using a One-To-One Link
class Profile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = models.CharField(max_length=30, required=False, help_text='Optional.')
    email = models.EmailField(max_length=160, help_text='Required. Inform a valid email address.')
    zip = models.CharField(max_length=6, required=True, help_text='Required')
    state = models.CharField(max_length=2, required=True)
    city = models.CharField(max_length=30, required=True)
    address_1 = models.CharField(max_length=50, required=True)
    address_2 = models.CharField(max_length=50, required=True)


def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

post_save.connect(create_user_profile, sender=User)
post_save.connect(save_user_profile, sender=User)