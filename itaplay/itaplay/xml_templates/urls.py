from . import views
from django.conf.urls import url


urlpatterns = [
    url(r'^all/', views.TemplateView.as_view()),
    url(r'^add/', views.TemplateView.as_view()),
    url(r'delete/(?P<template_id>\d+)$', views.TemplateView.as_view()),
    url(r'current/(?P<template_id>\d+)$', views.TemplateView.as_view()),
]
