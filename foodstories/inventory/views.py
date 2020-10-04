from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView

from inventory.models import Recipe, Comments, User


class RecipeView(ListView):
    model = Recipe
    context_object_name = 'recipe_list'
    queryset = Recipe.objects.order_by('-id')
    template_name = 'recipes.html'
    paginate_by = 3

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['author'] = User.objects.first()
        return context

class RecipeDetailView(DetailView):
    model = Recipe
    context_object_name = 'recipe_detail'
    queryset = Recipe.objects.all()
    template_name = 'single.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class IndexView(ListView):
    model = Recipe
    # template_name_list = [['index.html', 'single.html']]
    queryset = Recipe.objects.order_by('-id')[:4]
    context_object_name = 'index_recipes'
    # template_name = 'index.html'

    def get_template_names(self):
        return ['index.html']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['first'] = Recipe.objects.order_by('-id')[0]
        context['author'] = User.objects.first()
        return context
