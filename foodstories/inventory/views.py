from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView

from inventory.models import Recipe, Comments, User, Category


class RecipeView(ListView):
    model = Recipe
    context_object_name = 'recipe_list'
    queryset = Recipe.objects.order_by('-id')
    template_name = 'recipes.html'
    paginate_by = 3

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['author'] = User.objects.first()
        context['category'] = Category.objects.all()[:3]
        return context

class RecipeDetailView(DetailView):
    model = Recipe
    context_object_name = 'recipe_detail'
    queryset = Recipe.objects.all()
    template_name = 'single.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['recent'] = Recipe.objects.order_by('-id')[:3]
        context['category'] = Category.objects.all()[:6]
        return context

class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['first'] = Recipe.objects.order_by('-id')[0]
        context['author'] = User.objects.first()
        context['index_recipes'] = Recipe.objects.order_by('-id')[:4]
        context['holidays_recipes'] = Recipe.objects.all()[:2]
        context['category'] = Category.objects.all()[:6]
        return context

class ContactView(TemplateView):
    template_name = 'contact.html'

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     return context

class AboutView(TemplateView):
    template_name = 'about.html'
