from . import views
from django.conf.urls import url


urlpatterns = [
    url(r'^all/', views.xml_templates_list),
    url(r'^add/', views.xml_templates_add),
    url(r'^delete/(?P<pk>\d+)$', views.xml_template_delete),
    url(r'^current/(?P<pk>\d+)$', views.xml_template_current),
]

    # url(r'^all/', views.TemplateView.as_view()),
    # url(r'^add/', views.TemplateView.as_view()),
    # url(r'delete/(?P<pk>\d+)$', views.TemplateView.as_view()),
    # url(r'current/(?P<pk>\d+)$', views.TemplateView.as_view())
