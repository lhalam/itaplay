from django.conf.urls import include, url
from django.contrib import admin


urlpatterns = [
    url(r'^', include('home.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^company/', include('company.urls')),
    url(r'^player/', include('player.urls')),
]

