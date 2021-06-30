from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('account/registration/', views.Registration.as_view(), name='registration'),
    path('account/login/', views.userlogin, name='login'),
    path('account/logout/', views.userlogout, name='logout'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('doctor_list/', views.doctor_list, name='doctor_list'),
    path('delete_doctor/<int:id>', views.delete_doctor, name='delete_doctor'),
    path('edit_doctor/<int:id>', views.edit_doctor, name='edit_doctor'),
    path('view_doctor/<int:id>', views.view_doctor, name='view_doctor'),
    path('patient_list/', views.patient_list, name='patient_list'),
]