from django.contrib import admin
from .models import ContactQuery
# Register your models here.


@admin.register(ContactQuery)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['id', 'email', 'related', 'subject', 'message']
