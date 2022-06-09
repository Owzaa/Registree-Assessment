from django.urls import path
from . import views

urlpatterns = [
    #Dashboard view
    path('', views.homeView, name='homeView'),
    path('Dashboard/', views.DashboardTable, name='Dashbaord')
]