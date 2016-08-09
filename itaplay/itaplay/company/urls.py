from . import views
from django.conf.urls import url


urlpatterns = [
    url(r'^company_get/', views.company_get),
    url(r'^company_post/', views.company_post),
]
