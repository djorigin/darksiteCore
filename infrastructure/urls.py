"""
URLs for the infrastructure app

"""

from django.urls import path
from . import views

app_name = 'infrastructure'

urlpatterns = [ 
    path('', views.index, name='index'),
    
]