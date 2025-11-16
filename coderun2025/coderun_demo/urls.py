from .views import hello, hello_with_templates
from django.urls import path

urlpatterns = [
    path('index',hello),
    path('index-template',hello_with_templates)
]
