from django.contrib import admin
from chat.models import Room, Message


class MessageAdmin(admin.ModelAdmin):
    list_display = ('sender', 'receiver', 'created_at')

admin.site.register(Message, MessageAdmin)


class RoomAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_by', 'created_at')

admin.site.register(Room, RoomAdmin)
