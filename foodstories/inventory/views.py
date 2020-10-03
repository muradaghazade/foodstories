from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView

from inventory.models import Recipe, Comments


class RecipeView(ListView):
    model = Recipe
    context_object_name = 'recipe_list'
    queryset = Recipe.objects.order_by('-id')
    template_name = 'recipes.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['murad'] = 'Murad'
        return context




















# def index(request):
#     recipes = Recipe.objects.order_by('-id')
#     context = {
#         'recipes': recipes
#     }
#     return render(request, 'index.html', context)

# def recipes(request):
#     return render(request, 'recipes.html')