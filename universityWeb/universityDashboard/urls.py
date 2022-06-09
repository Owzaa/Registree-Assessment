from django.urls import path
from . import views

urlpatterns = [
    #Dashboard view
    path('', views.dashView, name='dashView')
]