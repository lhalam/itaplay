from django.conf.urls import patterns, url
from . import views


urlpatterns = patterns(
    '',
    url(r'^register', views.register),
    url(r'^logout', views.logout),
    url(r'^', views.custom_login),
    url(r'^login', views.login)
)
