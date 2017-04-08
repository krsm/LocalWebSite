"""Defines url patterns for users."""

from django.conf.urls import include, url

from .views import home_page

urlpatterns = [
    # TODO move to a new page
    url(r'^$', home_page, name='index'),

    # # Login page.
    # url(r'^login/$', views.user_login, name='login'),
    #
    # # Logout page.
    # url(r'^logout/$', views.user_logout, name='logout'),
    #
    # # Registration page.
    # url(r'^register/$', views.register, name='register'),

    # url(r'^__debug__/', include(debug_toolbar.urls)),

]