from django.urls import path 
from .import views

urlpatterns = [
   path('', views.home, name='home'),
   path('participants',views.participants, name='participants'),
   # path('add_participants', views.add_participants, name='add_participants'),
   path('attendees', views.attendees, name='attendees'),
    path('add_participant', views.add_participant, name='add_participant'),  # Uncomment this line if you want to add participants via a form in your templates.
]