from django.urls import path

from . import views

app_name = 'inventory'

from inventory.views import RecipeView

urlpatterns = [
    path('', views.IndexView.as_view(), name='index-page'),
    path('recipes/', views.RecipeView.as_view(), name='recipe-list'),
    path('recipes/<int:pk>/', views.RecipeDetailView.as_view(), name='recipe'),
    path('contact/', views.ContactView.as_view(), name='contact'),
    path('create-story/', views.CreateRecipeView.as_view(), name='create_story'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('edit-story/<int:pk>/', views.EditRecipeView.as_view(), name='edit_story'),
    path('delete-story/<int:pk>/', views.DeleteRecipeView.as_view(), name='delete_story'),
    
]
