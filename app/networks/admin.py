from django.contrib import admin

from .models import Port, Rack, Stack, Switch, vLan


class SwitchAdmin(admin.ModelAdmin):
    list_display = ["name", "serial_number", "rack", "stack", "number_in_stack", "sort"]
    list_editable = [
        "sort",
        "rack",
        "stack",
        "number_in_stack",
    ]


admin.site.register(Rack)
admin.site.register(Stack)
admin.site.register(Switch, SwitchAdmin)
admin.site.register(Port)
admin.site.register(vLan)


# list_display_links = ["id", "name"]
# list_filter = ["rack", "stack", "switch_type"]
# search_fields = ["name", "ip_address"]
# list_per_page = 25
