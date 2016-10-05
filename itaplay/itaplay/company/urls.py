from . import views
from django.conf.urls import url


urlpatterns = [
    url(r'^company_list_view/', views.CompanyListView.as_view(), name='company_list_view'),
    url(r'^company_details_view/(?P<company_id>\d+)/', views.CompanyDetailsView.as_view(), name='company_details_view'),
]

