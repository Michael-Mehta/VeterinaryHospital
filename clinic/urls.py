from django.urls import path
from .views import simple_test, simple_test_post



urlpatterns = [
    path('test/', simple_test),
    path('test-post/', simple_test_post)
]
