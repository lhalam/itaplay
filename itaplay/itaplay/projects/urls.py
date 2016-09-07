from . import views
from django.conf.urls import url


urlpatterns = [
    url(r'^projects/add_project_template/', views.AdviserProjectView.as_view()),
    url(r'^projects/$', views.AdviserProjectList.as_view()),
    url(r'^projects/(?P<id>\d+)/$', views.AdviserProjectDetails.as_view())
]
