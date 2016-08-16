from django.contrib import admin

from authentication.models import AdviserUser, AdviserInvitations


class AdviserUserAdmin(admin.ModelAdmin):
    list_display = ('user', 'id_company', 'avatar')


class AdviserIvitationAdmin(admin.ModelAdmin):
    list_display = ('email', 'id_company', 'is_active')

admin.site.register(AdviserUser, AdviserUserAdmin)
admin.site.register(AdviserInvitations, AdviserIvitationAdmin)
