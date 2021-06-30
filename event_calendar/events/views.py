from django.shortcuts import render, redirect
from .models import Event
from .forms import EventForm

# Create your views here.


def list_events(request):
    events = Event.objects.all()
    context = {'events': events}
    return render(request, 'events/events_list.html', context)


def show_event(request, event_id):
    event = Event.objects.get(id=event_id)
    context = {'event': event}
    return render(request, 'events/event_detail.html', context)


# A subclass of ModelForm can accept an existing model instance as the keyword argument instance; if this is supplied, YourForm.save() will update that instance. If it’s not supplied, YourForm.save() will create a new instance of the specified model.


def create_event(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            new_event = form.save()
            return redirect('events:show_event', event_id=new_event.id)
    else:  # if request is GET, we create a blank form and display it
        event_form = EventForm()
        context = {'event_form': event_form}
        return render(request, 'events/create_event.html', context)


def edit_event(request, event_id):
    event = Event.objects.get(id=event_id)
    if request.method == 'POST':
        # Passing in instance of unedited_event b/c we want to edit that instance with the POST data.
        form = EventForm(request.POST, instance=event)
        if form.is_valid():
            event = form.save()
            event.save()
            return redirect('events:show_event', event_id=event.id)
    else:  # if request is GET
        event_form = EventForm(instance=event)
        context = {'event_form': event_form}
        return render(request, 'events/create_event.html', context)


def delete_event(request, event_id):
    event = Event.objects.get(id=event_id)
    event.delete()
    return redirect('events:list_events')
