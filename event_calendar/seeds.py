from events.models import Event

Event.objects.all().delete()

e1 = Event(name="Pool Tournament")
e1.description = "Reno is going to dominate this tournament."
e1.created_at = "2021-07-07 00:00:00"
e1.starts_at = "2021-07-10 08:00:00"
e1.ends_at = "2021-07-10 22:00:00"

e1.save()

e1 = Event(name="2nd Birthday Party")
e1.description = "A Mickey Mouse themed birthday bash!"
e1.created_at = "2021-07-03"
e1.starts_at = "2021-07-04 12:00:00"
e1.ends_at = "2021-07-04 15:00:00"

e1.save()