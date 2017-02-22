"""Defines url patterns for users."""

from django.conf.urls import url
from django.contrib.auth.views import login

from . import views

urlpatterns = [
    # TODO move to a new page
    url(r'^$', views.home_page, name='index'),

    # Login page.
    url(r'^login/$', views.user_login, name='login'),

    # Logout page.
    url(r'^logout/$', views.user_logout, name='logout'),

    # Registration page.
    url(r'^register/$', views.register, name='register'),

]