"""Defines url patterns for users."""

from django.conf.urls import url
from django.contrib.auth.views import login

from . import views

urlpatterns = [
    # TODO move to a new page
    url(r'^$', views.index, name='index'),

    # Login page.
    url(r'^login/$', login, {'template_name': 'login.html'},
        name='login'),

    # Logout page.
    url(r'^logout/$', views.logout_view, name='logout'),

    # Registration page.
    url(r'^register/$', views.register, name='register'),

]