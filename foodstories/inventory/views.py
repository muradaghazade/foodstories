from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView, DetailView

from inventory.models import Recipe, Comments


class RecipeView(ListView):
    model = Recipe
    context_object_name = 'recipe_list'
    queryset = Recipe.objects.order_by('-id')
    template_name = 'recipes.html'
    # paginate_by = 3

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['murad'] = 'Murad'
        return context

class RecipeDetailView(DetailView):
    model = Recipe
    context_object_name = 'recipe_detail'
    queryset = Recipe.objects.all()
    template_name = 'single.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
