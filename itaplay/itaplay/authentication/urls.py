from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^register', views.RegistrationView.as_view()),
    url(r'^invite', views.InviteView.as_view()),
    url(r'^login', views.LoginView.as_view()),
    url(r'^logout', views.LogoutView.as_view())
]
