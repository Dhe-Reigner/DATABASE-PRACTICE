from django.shortcuts import render
from . models import Event
from . models import Participant 

# Create your views here.
def home(request):
    all_events =Event.objects.all()
    return render(request, 'home.html', {
        'merry':all_events
    })

def participants(request):
    all_participants = Participant.objects.all()
    return render(request, 'participants.html',{
        'attendants':all_participants
    })