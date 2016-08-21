from . import views
from django.conf.urls import url


urlpatterns = [
    url(r'^all/', views.xml_templates_list),
    url(r'^add/', views.xml_templates_add),
    url(r'delete/(?P<pk>\d+)$', views.xml_template_delete),
]
