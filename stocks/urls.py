from django.urls import path
from . import views
urlpatterns = [
   path(r'view/', views.party_name),
   path(r'get_data/',views.display),
   path(r'<int:question_id>/<str:name>/del/',views.delete),
   path(r'add/',views.add),
   path(r'submit/',views.submit),
   path(r'<int:lot_id>/edit/',views.edit),
   path(r'edit_submit/',views.update),
]