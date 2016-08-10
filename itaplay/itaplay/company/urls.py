from . import views
from django.conf.urls import url


urlpatterns = [
    url(r'^company_get/', views.company_get),
    url(r'^company_post/', views.company_post),
    url(r'^delete_company/', views.delete_company),
    url(r'^edit_company/', views.edit_company),
    url(r'^get_current/(?P<company_id>\d+)/', views.current_company),

]
