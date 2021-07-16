from django.urls import path, include
from events import views

app_name = "events"

urlpatterns = [
    path("", views.index, name="index"),
    path("event/<int:event_id>", views.event_detail, name="event_detail"),
    path("event/<int:event_id>/update", views.event_update, name="event_update"),
    path("event/<int:event_id>/delete", views.event_delete, name="event_delete"),
    path("create", views.event_create, name="event_create")
]