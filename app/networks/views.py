from django.shortcuts import render
from django.views.generic import CreateView, DetailView, ListView, UpdateView

from .forms import PortForm
from .models import Port, Rack, Stack, Switch


class RackListView(ListView):
    model = Rack
    projects = Port.objects.filter(status__icontains="projects")
    extra_context = {"projects": projects}


class PortCreateView(CreateView):
    model = Port
    form_class = PortForm
    success_url = "/"


class PortUpdateView(UpdateView):
    model = Port
    form_class = PortForm


class RackDetailView(DetailView):
    model = Rack


class SwitchDetail(DetailView):
    model = Switch


class PortDetail(DetailView):
    model = Port
    
