from django.contrib import admin

from .models import Network, Port, Rack, Stack, Switch

admin.site.register(Rack)
admin.site.register(Stack)
admin.site.register(Switch)
admin.site.register(Network)
admin.site.register(Port)
