from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView

from .models import Link


class LinkListView(ListView):
    model = Link


class LinkCreateView(CreateView):
    model = Link
    fields = ['url']


class LinkUpdateView(UpdateView):
    model = Link
    fields = ['url']
