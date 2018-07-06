from django.urls import path

from . import views
urlpatterns = [
   path(r'', views.display),
   path(r'get_data/',views.get_data),
   path(r'get_commodity_data/',views.get_commodity_data),
   path(r'get_comm_bal/',views.display_com),
   path(r'get_bal/',views.get_commodity_balance),
]