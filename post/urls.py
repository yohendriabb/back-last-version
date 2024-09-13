from django.urls import path 
from .api import (
    post_list, 
    doctor_list,
    specialty_list,
    post_create,
    date_create, 
    services_list, 
    date_list, 
    specialty_create, 
    doctor_create,
    services_detail
)


urlpatterns = [
     path('', post_list, name="post_list"),
     path('doc-list/', doctor_list, name="doc-list"),
     path('specialty-list/', specialty_list, name="especialty-list"),
     path('reserve-create/', post_create, name='create-post'),
     path('date-create/', date_create, name="date-create"),
     path('doctor-create/', doctor_create, name="doctor-create"),
     path('specialty-create/', specialty_create, name="specialty-create"),
     path('date-list/', date_list, name="date-list"),
     path('services/', services_list, name="services-list"),
     path('services-detail/<slug:slug>/', services_detail, name="services-detail"),
     
]