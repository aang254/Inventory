from django.urls import path
from . import views


urlpatterns = [
   path(r'add/', views.gatepass),
   path(r'get_details/',views.getdata, name='data'),
   path(r'submit_gatepass/',views.submit, name='Gatepass Submitted'),
   path(r'submit_edit_gatepass/',views.submit_edit),
   path('view/',views.view),
   path(r'edit_gatepass/',views.edit),
   path(r'<int:question_id>/del/',views.delete),
]