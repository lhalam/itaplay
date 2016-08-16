from . import views
from django.conf.urls import url


urlpatterns = [
    url(r'^company_view/', views.CompanyView.as_view()),
    url(r'^current_company_view/(?P<company_id>\d+)/', views.CompanyView.as_view()),
    url(r'^delete_company/(?P<company_id>\d+)/', views.CompanyView.as_view()),
]

