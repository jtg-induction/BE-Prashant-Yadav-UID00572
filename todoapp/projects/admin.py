from django.contrib import admin

from projects.models import Project


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'max_members', 'status')


admin.site.register(Project,ProjectAdmin)
