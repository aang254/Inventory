from django.contrib import admin
from .models import Stocks

admin.site.site_header = 'Warehouse Management System'


# Register your models here.
admin.site.register(Stocks)
