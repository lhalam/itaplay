from django.conf.urls import url
from xml_templates import views


urlpatterns = [
    url(r'^all/', views.TemplateView.as_view(), name='templates_list'),
    url(r'^add/', views.TemplateView.as_view(), name='template_add'),
    url(r'delete/(?P<template_id>\d+)$',
        views.TemplateView.as_view(), name='template_delete'),
    url(r'current/(?P<template_id>\d+)$',
        views.TemplateView.as_view(), name='template_current'),
]
