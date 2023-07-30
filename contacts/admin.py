from django.contrib import admin
from .models import Contact


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Contact._meta.fields]
    list_display_links = ["email"]
    search_fields = ["email"]
    list_filter = ["created_date"]

    class Meta:
        model = Contact