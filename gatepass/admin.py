from django.contrib import admin
from .models import gate_pass

admin.site.site_header = 'Warehouse Management System'


class GatePassAdmin(admin.ModelAdmin):
    list_display = ('passNo','lot','date','Name','commodity','bags','boxes')

# Register your models here.
admin.site.register(gate_pass,GatePassAdmin)
