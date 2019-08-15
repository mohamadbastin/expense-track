"""Expense_Track URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from rest_framework.authtoken import views
from assets.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-token-auth/', views.obtain_auth_token),
    path('signup/', SignUpView.as_view()),
    path('budget/create/', BudgetCreateView.as_view()),
    path('budget/list/', BudgetListView.as_view()),
    path('category/create/', CategoryCreateView.as_view()),
    path('category/list/', CategoryListView.as_view()),
    path('expense/create/', ExpenseCreateView.as_view()),
    path('expense/list/', ExpenseListView.as_view()),
    path('expense/list/category/<int:pk>/', CategorySpentListView.as_view()),
    path('expense/list/budget/<int:pk>/', BudgetSpentListView.as_view()),
    path('tokencheck/', TokenValidate.as_view())

]
