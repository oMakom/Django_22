from django.contrib import admin

from users.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'username', 'first_name', 'last_name', 'avatar', 'phone_number')
    list_filter = ("username", "email")
    search_fields = ("username", "email")
