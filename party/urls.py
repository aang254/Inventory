from django.urls import path
from . import views
urlpatterns = [
   path(r'add/', views.add),
]