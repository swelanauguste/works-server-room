from django.contrib import admin

from .models import Port, Rack, Stack, Switch, vLan

admin.site.register(Rack)
admin.site.register(Stack)
admin.site.register(Switch)
admin.site.register(Port)
admin.site.register(vLan)
