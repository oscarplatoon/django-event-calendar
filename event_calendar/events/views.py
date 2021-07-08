from django.shortcuts import render, redirect
from .models import Event
from .forms import EventForm

# Create your views here.


def list_events(request):
    if request.user.is_authenticated:
        events = Event.objects.filter(author=request.user)
        context = {'events': events}
    else:
        context = {}

    return render(request, 'events/events_list.html', context)


def show_event(request, event_id):
    if request.user.is_authenticated:
        event = Event.objects.get(id=event_id)
        if event.author == request.user:
            context = {'event': event}
            return render(request, 'events/event_detail.html', context)

    return redirect('events:list_events')


# A subclass of ModelForm can accept an existing model instance as the keyword argument instance; if this is supplied, YourForm.save() will update that instance. If it’s not supplied, YourForm.save() will create a new instance of the specified model.


def create_event(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            new_event = form.save(commit=False)
            new_event.author = request.user
            new_event.save()  # commit=True by default. Saves it to db
            return redirect('events:show_event', event_id=new_event.id)

    # if request is GET or form is not valid, we create a blank form and display it
    event_form = EventForm()
    context = {'event_form': event_form, 'type': 'Create'}
    return render(request, 'events/event_form.html', context)


def edit_event(request, event_id):
    event = Event.objects.get(id=event_id)
    if request.method == 'POST':
        # Passing in instance of event b/c we want to edit that instance with the POST data.
        form = EventForm(request.POST, instance=event)
        if form.is_valid():
            # does the same thing as calling .save() on an Event instance
            edited_event = form.save(commit=False)
            edited_event.author = request.user
            edited_event.save()
            return redirect('events:show_event', event_id=event_id)

    # if request is GET or form is not valid
    event_form = EventForm(instance=event)
    context = {'event_form': event_form, 'type': 'Edit'}
    return render(request, 'events/event_form.html', context)


def delete_event(request, event_id):
    event = Event.objects.get(id=event_id)
    event.delete()
    return redirect('events:list_events')
