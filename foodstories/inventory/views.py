from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView, CreateView, UpdateView, DeleteView

from inventory.models import Recipe, Comments, User, Category, ContactUs, Tag
from .forms import ContactUsForm, CreateRecipeForm, CreateCommentForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic.edit import FormMixin
from django.core.exceptions import PermissionDenied

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

class RecipeDetailView(FormMixin, DetailView):
    model = Recipe
    context_object_name = 'recipe_detail'
    queryset = Recipe.objects.all()
    form_class = CreateCommentForm
    template_name = 'single.html'

    def get_success_url(self):
        return reverse_lazy('inventory:recipe', kwargs={'pk':self.get_object().id})

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['recent'] = Recipe.objects.order_by('-id')[:3]
        context['category'] = Category.objects.all()[:6]
        context['tags'] = Tag.objects.all()
        context['len'] = len(Recipe.objects.all())
        return context

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.recipes = self.get_object()
        form.save()
        return super().form_valid(form)

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

class ContactView(CreateView):
    model = ContactUs
    template_name = 'contact.html'
    form_class = ContactUsForm
    success_url = reverse_lazy('inventory:contact')

class CreateRecipeView(LoginRequiredMixin, CreateView):
    model = Recipe
    template_name = 'create_story.html'
    form_class = CreateRecipeForm
    success_url = reverse_lazy('inventory:recipe-list')

    # def post(self, request, *args, **kwargs):
    #     print('1-----------', self.get_form().data.description)
    #     if self.get_form().is_valid():
    #         print('2----------')
    #     else:
    #         print('3----------')

    #     return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class EditRecipeView(UpdateView):
    model = Recipe
    template_name = 'update_story.html'
    form_class = CreateRecipeForm
    success_url = reverse_lazy('inventory:recipe-list')

    def dispatch(self, request, *args, **kwargs):
        if self.request.user != self.get_object().author:
            raise PermissionDenied
        return super(EditRecipeView, self).dispatch(request, *args, **kwargs)


class DeleteRecipeView(DeleteView):
    model = Recipe
    template_name = 'delete.html'
    success_url = reverse_lazy('inventory:recipe-list')

class AboutView(TemplateView):
    template_name = 'about.html'




