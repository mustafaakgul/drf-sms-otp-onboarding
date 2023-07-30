from django.contrib import admin
from .models import PendingUser, User, Token


@admin.register(PendingUser)
class PendingUserAdmin(admin.ModelAdmin):
    list_display = [field.name for field in PendingUser._meta.fields]
    list_display_links = ["phone"]
    search_fields = ["phone"]
    list_filter = ["created_at"]

    class Meta:
        model = PendingUser


@admin.register(Token)
class TokenAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Token._meta.fields]
    list_display_links = ["user", "token"]
    search_fields = ["user", "token"]
    list_filter = ["created_at"]

    class Meta:
        model = Token


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = [field.name for field in User._meta.fields]
    list_display_links = ["email", "phone"]
    search_fields = ["email", "phone"]
    list_filter = ["created_at"]

    class Meta:
        model = User