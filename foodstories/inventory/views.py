from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.list import ListView

from inventory.models import Recipe, Comments


class RecipeView(ListView):
    model = Recipe
    context_object_name = 'recipe_list'
    queryset = Recipe.objects.order_by('-id')
    template_name = 'templates/test.html'

    def get_context(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context




















# def index(request):
#     recipes = Recipe.objects.order_by('-id')
#     context = {
#         'recipes': recipes
#     }
#     return render(request, 'index.html', context)

# def recipes(request):
#     return render(request, 'recipes.html')