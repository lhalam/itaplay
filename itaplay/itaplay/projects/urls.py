from . import views
from django.conf.urls import url


urlpatterns = [
    url(r'^projects/$', views.AdviserProjectList.as_view(), name="projects-list"),
    url(r'^projects/(?P<pk>\d+)/$', views.AdviserProjectDetails.as_view(), name="project"),
    url(r'^projects/\d+/template/$', views.AdviserProjectView.as_view()),
]
