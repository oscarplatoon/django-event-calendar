from django.urls import path
from . import views

app_name = 'events'

urlpatterns = [
    path('', views.list_events, name='list_events'),
    path('<int:event_id>/', views.show_event, name='show_event'),
    path('new/', views.create_event, name='create_event'),
    path('<int:event_id>/edit/', views.edit_event, name='edit_event'),
    path('<int:event_id>/delete/', views.delete_event, name='delete_event'),
]
