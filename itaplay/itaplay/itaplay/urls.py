"""itaplay URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include, patterns
from django.conf.urls.static import static
from django.contrib import admin
from .settings import MEDIA_ROOT, DEBUG

urlpatterns = [
    url(r'^', include('home.urls')),
    url(r'^', include('home.urls')),
    url(r'^clips/', include('clips.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^auth/', include('authentication.urls')),
    url(r'^company/', include('company.urls')),
    url(r'^templates/', include('xml_templates.urls')),
    url(r'^player/', include('player.urls')),
    url(r'^monitor/', include('monitor.urls')),
    url(r'^api/', include('projects.urls')),
]


if DEBUG:
    # serve files from media folder
    urlpatterns.append(
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': MEDIA_ROOT}))
