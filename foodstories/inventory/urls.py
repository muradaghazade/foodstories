from django.urls import path

from . import views

app_name = 'inventory'

from inventory.views import RecipeView

urlpatterns = [
    path('', views.IndexView.as_view(), name='index-page'),
    path('recipes/', views.RecipeView.as_view(), name='recipe-list'),
    path('recipes/<int:pk>/', views.RecipeDetailView.as_view(), name='recipe')
]


# urlpatterns = [
#     path('', views.index, name='index'),
#     path('recipes', views.recipes, name='recipes'),
# ]