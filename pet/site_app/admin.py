from django.contrib import admin
from .models import Contact, CustomUser


@admin.register(Contact)
class AdminContact(admin.ModelAdmin):
    list_display = ('email', 'address', 'phone')


@admin.register(CustomUser)
class AdminCustomUser(admin.ModelAdmin):
    list_display = ['id', 'about']
