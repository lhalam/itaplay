from django.contrib import admin

from authentication.models import AdviserUser, AdviserInvitations

admin.site.register(AdviserUser)

admin.site.register(AdviserInvitations)
