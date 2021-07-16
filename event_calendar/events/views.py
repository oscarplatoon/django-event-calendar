from django.shortcuts import render
from django.http import HttpResponse
from events.models import Event
from events.forms import EventForm

def index(request):
    data = {
        "all_events": Event.objects.all()
    } 

    return render(request, "events/index.html", data)


def event_detail(request, event_id):
    event = Event.objects.get(pk=event_id)
    if not event:
        HttpResponse("HEY, that event doesn't exist")
    
    data = {
        "my_event": event 
    } 
    # add in template name
    return render(request, "events/detail.html", data)


def event_create(request):
    return process_event_form(request)


def event_update(request, event_id):
    try:
        return process_event_form(request, event_id)
    except:
        return HttpResponse("Event doesn't exist")
    

def process_event_form(request, event_id=None):
    event = Event.objects.get(pk=event_id) if event_id is not None else None
    event_form = EventForm(request.POST or None, instance=event)

    if request.method == "POST":
        try:
            event_form.save()
            return HttpResponse("New Event Created!!" if event_id is None else "Updated event!")
        except Exception as e:
            print(e)
            return HttpResponse("Error with event processing.")

    data = {
        "event_form": event_form,
        "create_or_update": event_id is None
    }

    return render(request, "events/form.html", data)


def event_delete(request, event_id):
    try:
        event = Event.objects.get(pk=event_id)
        if event:
            event.delete()
            return HttpResponse("Event removed!!")
    except:
        return HttpResponse("Event doesn't exist")

