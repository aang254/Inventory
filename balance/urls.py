from django.urls import path

from . import views
urlpatterns = [
   path(r'', views.display),
   path(r'get_data/',views.get_data),
]