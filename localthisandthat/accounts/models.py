from django.db import models
from django.contrib.auth.models import User
# Signals
from django.db.models.signals import post_save
from django.dispatch import receiver


#  Extending User Model Using a One-To-One Link
class Profile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = models.CharField(max_length=30, required=False, help_text='Optional.')
    email = models.EmailField(max_length=160, default='', help_text='Required. Inform a valid email address.')
    zip = models.CharField(max_length=6, default='', required=True, help_text='Required')
    state = models.CharField(max_length=2, default='', required=True)
    city = models.CharField(max_length=30, default='', required=True)
    addrres_1 = models.CharField(max_length=50, default='', required=True)
    addrres_2 = models.CharField(max_length=50, default='', required=True)
    date_joined = models.DateTimeField(_('date joined'), auto_now_add=True)
    is_active = models.BooleanField(_('active'), default=True)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()