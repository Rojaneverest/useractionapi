# user_action_project/urls.py

from django.urls import path, include

urlpatterns = [
    # Other paths or URLs from other apps
    path('user_actions_app/', include('user_actions_app.urls')),  # Adjust 'your_app' accordingly
]
