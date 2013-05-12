from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic

from .models import CarModel, Manufacturer


class ListView(generic.ListView):
    model = CarModel

class DetailView(generic.DetailView):
    model = CarModel

