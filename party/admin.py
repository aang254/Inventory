from django.contrib import admin
from .models import party_Ledger

admin.site.site_header = 'Warehouse Management System'


# Register your models here.
admin.site.register(party_Ledger)
