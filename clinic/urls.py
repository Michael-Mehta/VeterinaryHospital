from django.urls import path
from .views import *



urlpatterns = [
    #Test
    path('test/', simple_test),
    path('test-post/', simple_test_post),

    #GET
    path('owners/', return_all_owners),
    path('owners/<int:owner_id>/pets/', return_all_pets_by_owner),
    path('pets/all/', return_all_pets),
    path('vets/all/', return_all_vets),
    path('appointments/all/', return_all_appointments),

    #POST
    path('owners/create/', create_owner),
    path('pets/create/', create_pet),
    path('vets/create/', create_vet),
    path('appointments/create/', create_appointment),

    #DELETE
    path('owners/delete/<int:owner_id>/', delete_owner),
    path('pets/delete/<int:pet_id>/', delete_pet),
    path('vets/delete/<int:vet_id>/', delete_vet),
    path('appointments/delete/<int:appointment_id>/', delete_appointment),

    #PATCH
    path('owners/update/<int:owner_id>/', update_owner),
    path('appointments/update/<int:appointment_id>/', update_appointment),


    #PUT only because I am using images here and form-data works better with PUT requests
    path('pet/update/<int:pet_id>/', update_pet),
    path('vet/update/<int:vet_id>/', update_vet)

    
]
