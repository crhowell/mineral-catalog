import random

from django.core.urlresolvers import reverse
from django.shortcuts import redirect
from django.views import generic
from . import models


class HomepageView(generic.TemplateView):
    template_name = 'index.html'


class MineralListView(generic.ListView):
    model = models.Mineral
    template_name = 'index.html'
    context_object_name = 'mineral_list'


class MineralDetailView(generic.DetailView):
    model = models.Mineral
    template_name = 'detail.html'


class MineralRandomView(generic.View):

    def get(self, request, *args, **kwargs):
        minerals = models.Mineral.objects.only("pk")
        if minerals:
            mineral = random.choice(minerals)
            return redirect(reverse('detail', kwargs={'pk': mineral.pk}))
        return redirect(reverse('home'))







