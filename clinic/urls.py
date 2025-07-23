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

    #POST
    path('owners/create/', create_owner),
    path('pets/create/', create_pet),

    #DELETE
    path('owners/delete/<int:owner_id>/', delete_owner),
    path('pets/delete/<int:pet_id>/', delete_pet),

    #PATCH
    path('owners/update/<int:owner_id>/', update_owner),
    path('pet/update/<int:pet_id>/', update_pet)

    
]
