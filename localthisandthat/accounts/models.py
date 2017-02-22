from django.db import models
from django.contrib.auth.models import User
# Signals
from django.db.models.signals import post_save


#  Extending User Model Using a One-To-One Link
class Profile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=160)
    zip = models.CharField(max_length=6)
    state = models.CharField(max_length=2)
    city = models.CharField(max_length=30)
    address_1 = models.CharField(max_length=50)
    address_2 = models.CharField(max_length=50)
    timestamp = models.DateTimeField(auto_now=True)
    # TODO create last_login_timestamp

    def __str__(self):
        return self.user.first_name


# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         Profile.objects.create(user=instance)
#
#
# def save_user_profile(sender, instance, **kwargs):
#     instance.profile.save()
#
# # Action that is event driven
# post_save.connect(create_user_profile, sender=User)
# post_save.connect(save_user_profile, sender=User)