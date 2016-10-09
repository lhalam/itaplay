from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^all/$', views.AdviserUsersList.as_view(), name='allusers'),
    url(r'^all/(?P<pk>\d+)/$', views.AdviserUserDetails.as_view(), name="user"),
    url(r'invitations/$', views.InvitationView.as_view(), name='allinvitations'),
]
