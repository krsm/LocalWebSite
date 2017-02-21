from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from .form import UserForm, ProfileForm
# Create your views here.


def logout_view(request):
    """Log the user out."""
    logout(request)
    return HttpResponseRedirect(reverse('accounts:index'))


def register(request):
    """Register a new user."""
    # Boolean for telling the template, if the registration was ok
    registered = False
    if request.method != 'POST':
        # If it is not a HTTP POST
        # Display blank registration form.
        user_form = UserForm()
        profile_fom = ProfileForm()
    else:
        # Process completed form.
        user_form = UserForm(data=request.POST)
        profile_fom = ProfileForm(data=request.POST)
        # If
        if user_form.is_valid() and profile_fom.is_valid():
            # Save the new user data
            new_user = user_form.save()
            # Hashing, and and update the object
            new_user.set_password(new_user.password)
            new_user.save()

            # Profile form
            # commit=False to delay saving the model, to avoid integrity problems
            profile_fom = ProfileForm.save(commit=False)
            profile_fom.user = new_user

            # registration was successful
            registered = True
        else:
            # In case of invalid forms
            print('user_form.errors', user_form.errors)
            print('profile_fom.errors', profile_fom.errors)

            # TODO once registered is OK, load main page
            # return HttpResponseRedirect(reverse('accounts:index'))

    context = {'user_form': user_form,
               'profile_fom': profile_fom,
               'registered': registered
               }

    return render(request, 'register.html', context)
# #
#
# @login_required
# @transaction.atomic
# def update_profile(request):
#     if request.method == 'POST':
#         user_form = UserForm(request.POST, instance=request.user)
#         profile_form = ProfileForm(request.POST, instance=request.user.profile)
#         if user_form.is_valid() and profile_form.is_valid():
#             user_form.save()
#             profile_form.save()
#             messages.success(request, _('Your profile was successfully updated!'))
#             return redirect('settings:profile')
#         else:
#             messages.error(request, _('Please correct the error below.'))
#     else:
#         user_form = UserForm(instance=request.user)
#         profile_form = ProfileForm(instance=request.user.profile)
#     return render(request, 'profiles/profile.html', {
#         'user_form': user_form,
#         'profile_form': profile_form
#     })