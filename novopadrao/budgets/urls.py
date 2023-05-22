from django.urls import include, path
from . import views

urlpatterns = [
    
    path('budgets/', views.listBudgets, name='budgets-list'),
]
