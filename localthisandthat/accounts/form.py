from django import forms
from django.contrib.auth.models import User


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('url', 'location', 'company')

        # user = models.OneToOneField(User, on_delete=models.CASCADE)
        # first_name = models.CharField(max_length=30, required=False, help_text='Optional.')
        # last_name = models.CharField(max_length=30, required=False, help_text='Optional.')
        # email = models.EmailField(max_length=160, default='', help_text='Required. Inform a valid email address.')
        # zip = models.CharField(max_length=6, default='', required=True, help_text='Required')
        # state = models.CharField(max_length=2, default='', required=True)
        # city = models.CharField(max_length=30, default='', required=True)
        # addrres_1 = models.CharField(max_length=50, default='', required=True)
        # addrres_2 = models.CharField(max_length=50, default='', required=True)
        # date_joined = models.DateTimeField(_('date joined'), auto_now_add=True)
        # is_active = models.BooleanField(_('active'), default=True)
