from django.contrib import admin
from .models import Commodity

admin.site.site_header = 'Warehouse Management System'


# Register your models here.
admin.site.register(Commodity)

