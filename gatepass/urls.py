from django.urls import path
from . import views
urlpatterns = [
   path(r'add/', views.gatepass),
   path(r'data/',views.showdata, name='data'),
   path(r'submit_gatepass/',views.submit, name='Gatepass Submitted'),
   path(r'test_try/', views.test_form),
]