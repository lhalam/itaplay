from . import views
from django.conf.urls import url


urlpatterns = [
    url(r'^add_project_template/', views.AdviserProjectView.as_view()),
]