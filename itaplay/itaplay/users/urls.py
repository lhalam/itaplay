from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'all/$', views.UserView.as_view(), name='allusers'),
]
