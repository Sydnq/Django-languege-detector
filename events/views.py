from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from .models import Event


class EventListView(ListView):
    model = Event
    template_name = 'events/event_list.html'
    context_object_name = 'events'


class EventDetailView(DetailView):
    model = Event
    template_name = 'events/event_detail.html'
    context_object_name = 'event'
