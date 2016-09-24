import random

from django.core.urlresolvers import reverse
from django.shortcuts import redirect, get_list_or_404
from django.views import generic
from django.views.generic.base import ContextMixin

from . import models


ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

COLORS = ['red', 'blue', 'green', 'white', 'black',
          'gray', 'yellow', 'orange', 'purple']


class AlphabetNavMixin(ContextMixin):
    def get_context_data(self, **kwargs):
        context = super(AlphabetNavMixin, self).get_context_data(**kwargs)
        context['alpha_nav'] = ALPHABET
        return context


class GroupListMixin(ContextMixin):
    def get_context_data(self, **kwargs):
        context = super(GroupListMixin, self).get_context_data(**kwargs)
        context['group_list'] = models.Mineral.objects.values_list(
            'group', flat=True).distinct()
        return context


class ColorListMixin(ContextMixin):
    def get_context_data(self, **kwargs):
        context = super(ColorListMixin, self).get_context_data(**kwargs)
        context['color_list'] = COLORS
        return context


class MineralListView(generic.ListView,
                      AlphabetNavMixin, ColorListMixin, GroupListMixin):
    model = models.Mineral
    template_name = 'index.html'
    context_object_name = 'mineral_list'

    def get_queryset(self):
        return self.model.objects.filter(name__istartswith='a')


class MineralByLetterListView(MineralListView):
    def get_queryset(self):
        if 'name' in self.kwargs:
            if self.kwargs['name'][0] in ALPHABET:
                return self.model.objects.filter(
                    name__istartswith=self.kwargs['name'][0])
        return super().get_queryset()


class MineralByGroupListView(MineralListView):
    def get_queryset(self):
        group = self.kwargs['group'].replace('-', ' ')
        return self.model.objects.filter(group__iexact=group)


class MineralByColorListView(MineralListView):
    def get_queryset(self):
        color = self.kwargs['color']
        return self.model.objects.filter(color__icontains=color)


class MineralSearchForView(MineralListView):
    def get_queryset(self):
        search = self.request.GET.get('term')
        print(search)
        if search:
            return self.model.objects.filter(name__icontains=search)
        return self.model.objects.all()


class MineralDetailView(AlphabetNavMixin,
                        ColorListMixin, GroupListMixin, generic.DetailView):
    model = models.Mineral
    template_name = 'detail.html'


class MineralRandomView(AlphabetNavMixin,
                        ColorListMixin, GroupListMixin, generic.View):

    def get(self, request, *args, **kwargs):
        minerals = models.Mineral.objects.only("pk")
        if minerals:
            mineral = random.choice(minerals)
            return redirect(reverse('detail', kwargs={'pk': mineral.pk}))
        return redirect(reverse('home'))







