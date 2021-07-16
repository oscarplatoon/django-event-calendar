from django.forms import ModelForm
from events.models import Event

class EventForm(ModelForm):
    class Meta:
        model = Event
        fields = ["name", "description", "starts_at", "ends_at"]