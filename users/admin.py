from django.contrib import admin
from users.models import User


class UserAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'username', 'first_name', 'last_name',
        'email', 'phone_number', 'date_joined', 'is_staff', 'is_active', 'role'
    )
    list_display_links = ('username', 'first_name', 'last_name', 'email')
    search_fields = ('phone_number', 'email')


admin.site.register(User, UserAdmin)
