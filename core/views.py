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



