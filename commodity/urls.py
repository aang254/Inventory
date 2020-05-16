from django.urls import path
from . import views
urlpatterns = [
   path(r'view/', views.display),
   path(r'<int:question_id>/del/',views.delete),
   path(r'add/', views.commodity_add),
   path(r'submit/', views.submit)
]