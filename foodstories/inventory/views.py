from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render

from inventory.models import Recipe, Author, Comments, Reply

# Create your views here.
def index(request):
    return render(request, 'inventory/index.html')

def recipes(request):
    return render(request, 'inventory/recipes.html')