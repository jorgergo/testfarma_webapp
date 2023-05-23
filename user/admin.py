from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

# Register your models here.

class CustomUserAdmin(UserAdmin):
    model = User
    list_display = (
        'email', 'first_name', 'last_name','is_staff',
        )

    fieldsets = (
        (None, {
            'fields': ('email', 'password')
        }),
        ('Personal info', {
            'fields': ('first_name', 'last_name')
        }),
        ('Permissions', {
            'fields': (
                'is_active', 'is_staff', 'is_superuser',
                'groups', 'user_permissions', 'user_type',
                )
        }),
        ('Important dates', {
            'fields': ('last_login', 'date_joined')
        }),
        
    )

    add_fieldsets = (
        (None, {
            'fields': ('email', 'password1', 'password2')
        }),
        ('Personal info', {
            'fields': ('first_name', 'last_name')
        }),
        ('Permissions', {
            'fields': (
                'is_active', 'is_staff', 'is_superuser',
                'groups', 'user_permissions', 'user_type'
                )
        }),
        ('Important dates', {
            'fields': ('last_login', 'date_joined')
        }),
    )
    
    search_fields = ('email', 'first_name', 'last_name', 'is_staff')
    ordering = ('email',)


admin.site.register(User, CustomUserAdmin)