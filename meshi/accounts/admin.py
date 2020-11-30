from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from accounts.models import Account


class AccountAdmin(UserAdmin):
    list_display = (
        "id",
        "email",
        "username",
        "date_joined",
        "last_login",
        "is_admin",
        "is_staff",
        "is_superuser",
        "is_active"
    )
    search_fields = (
        "email",
        "username",
        "date_joined",
        "last_login",
        "is_admin",
        "is_staff",
        "is_superuser",
        "is_active"
    )
    readonly_fields = ("id", "date_joined", "last_login", "is_active")

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


admin.site.register(Account, AccountAdmin)
