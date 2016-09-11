from . import views
from django.conf.urls import url


urlpatterns = [
    url(r'^player_view/$', views.PlayerView.as_view()),
    url(r'^current_player_view/(?P<player_id>\d+)/', views.PlayerView.as_view()),
    url(r'^delete_player/(?P<player_id>\d+)/', views.PlayerView.as_view()),
]
	
