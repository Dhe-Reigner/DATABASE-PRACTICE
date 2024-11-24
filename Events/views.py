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
    
# def add_participant(request ):
#     if request.method == 'POST':
#         name = request.POST.get('name')
#         email = request.POST.get('email')
#         event_id = request.POST.get('event_id')
        
#         event = Event.objects.get(id=event_id)
#         participant = Participant(name=name, email=email, event=event)
#         participant.save()
        
#         return render(request, 'home.html', {
#             'merry':Event.objects.all()
#         })
#     else:
#         return render(request, 'add_participant.html')

def add_participant(request):
    return render(request, 'add_participant.html',{})


# def attendies(request):
#     event_id = request.GET.get('event_id')
#     event = Event.objects.get(id=event_id)
#     participants = Participant.objects.filter(event=event)
#     return render(request, 'attendies.html', {
#         'event': event,
#         'participants': participants
#     })
def attendees(request):
    return render(request, 'attendees.html', {})