from django.urls import path
from . import views
urlpatterns = [
   path(r'add/', views.add),
   path(r'view/', views.display),
   path(r'<int:question_id>/del/',views.delete),
   path(r'<int:question_id>/edit/',views.edit),
]