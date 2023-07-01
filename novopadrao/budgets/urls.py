from django.urls import include, path
from . import views

urlpatterns = [

    path('budgets/', views.listBudgets, name='budgets-list'),

    path('budgets/newBudget/', views.addBudgets, name='budgets-list'),

    path('budgets/budget/<int:id>', views.viewBudget, name='view-budget'),
    
    path('budgets/delete/<int:id>', views.deleteBudget, name='delete-budget'),
]
