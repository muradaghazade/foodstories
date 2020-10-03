from django.urls import path

from . import views

app_name = 'inventory'

from inventory.views import RecipeView

urlpatterns = [
    path('recipes', views.RecipeView.as_view(), name='recipe-list'),
]


# urlpatterns = [
#     path('', views.index, name='index'),
#     path('recipes', views.recipes, name='recipes'),
# ]