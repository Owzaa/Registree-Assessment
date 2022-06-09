from django.urls import path
from . import views

urlpatterns = [
    #Dashboard view
    path('', views.dashView, name='dashView'),
    path('UniversityDashboard/', views.DashboardTable, name='UniversityDashbaord')
]