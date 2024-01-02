# event_handler/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('record_user_action/', views.record_user_action, name='record_user_action'),
    # Other URL patterns if needed
]
