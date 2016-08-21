from . import views
from django.conf.urls import url


urlpatterns = [
    url(r'^all/', views.xml_templates_list),
    url(r'^add/', views.xml_templates_add),


]
