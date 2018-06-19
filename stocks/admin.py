from django.contrib import admin
from .models import Stocks

admin.site.site_header = 'Warehouse Management System'


class StocksAdmin(admin.ModelAdmin):
    list_display = ('lot','date','Name','commodity','begs','boxes')

# Register your models here.
admin.site.register(Stocks,StocksAdmin)
