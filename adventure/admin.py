from django.contrib import admin
from django.contrib.auth.models import Group
from .models import Room, Player

admin.site.site_header = 'Legends MUD API'


admin.site.register(Player)
admin.site.register(Room)
admin.site.unregister(Group)
