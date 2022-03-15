"""
Endpoint URLs for the IPEDS API.
"""

from django.urls import path
from . import views

urlpatterns = [
    path('ipeds-dict/', views.get_ipeds_dictionary)
]
