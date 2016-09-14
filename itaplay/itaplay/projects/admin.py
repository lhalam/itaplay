from django.contrib import admin

from projects.models import AdviserProject

class AdviserProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'id_company')

admin.site.register(AdviserProject, AdviserProjectAdmin)
