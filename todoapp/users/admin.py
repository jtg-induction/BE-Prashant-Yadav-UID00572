from django.contrib import admin

from users.models import CustomUser


class UserAdmin(admin.ModelAdmin):  
    list_display = ('id', 'first_name', 'last_name', 'email')


admin.site.register(CustomUser,UserAdmin)
