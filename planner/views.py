from django.shortcuts import render, redirect
from .models import Event

# Create your views here.
def index(request):
    events = Event.objects.all()
    return render(request, 'index.html', {'events': events})

def event_detail(request, title):
    event = Event.objects.get(title=title)
    return render(request, 'event_detail.html', {'event': event})

def add_event(request):
    if request.method == 'POST':
        new_event = Event(
            title = request.POST.get('title'),
            description = request.POST.get('description'),
            date = request.POST.get('date'),
            location = request.POST.get('location'),
        )
        new_event.save()
        return redirect('index')
    return render(request, 'add_event.html')