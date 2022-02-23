from django.contrib import admin
from core.models import User

# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("email", "last_login", "is_staff", "created")
    list_filter = ("last_login", "is_staff", "created")
    readonly_fields = ("created",)
    ordering = ("email",)
