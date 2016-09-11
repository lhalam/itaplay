from . import views
from django.conf.urls import url


urlpatterns = [
    url(r'^projects/$', views.AdviserProjectList.as_view()),
    url(r'^projects/(?P<pk>\d+)/$', views.AdviserProjectDetails.as_view()),
    url(r'^projects/\d+/template/$', views.AdviserProjectView.as_view()),
    url(r'^projects_to_players/$', views.AdviserProjectToPlayers.as_view()),
    url(r'^projects_to_players/(?P<project_id>\d+)/$', views.AdviserProjectToPlayers.as_view()),
]
