"""
URL configuration for project_7 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
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
from app_7 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('age/', views.AgeView.as_view()),
    path('percent/', views.PercentageView.as_view()),
    path('simple-interest/', views.SimpleInterest.as_view()),
    path('bmi/', views.BmiView.as_view()),
    path('bill/', views.BillView.as_view()),
    path('discount/', views.Discount.as_view()),
    path('profit/', views.ProfitView.as_view()),
    path('salary/', views.SalaryView.as_view()),
    path('time/', views.TimeConverter.as_view()),
    path('fuel/', views.FuelCost.as_view()),
    path('product-profit/', views.ProductProfit.as_view()),
    path('work-salary/', views.WorkSalary.as_view()),
    path('age-days/', views.AgeDays.as_view())
]
