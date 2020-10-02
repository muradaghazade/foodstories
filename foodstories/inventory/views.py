from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render

from inventory.models import Recipe, Comments

# Create your views here.
def index(request):
    recipes = Recipe.objects.order_by('-id')
    context = {
        'recipes': recipes
    }
    return render(request, 'inventory/index.html', context)

def recipes(request):
    return render(request, 'inventory/recipes.html')