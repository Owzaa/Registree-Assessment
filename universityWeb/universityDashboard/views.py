from django.shortcuts import render
from django.views.generic import TemplateView
import requests
import os
from .services import get_universitiesMarks, get_universitiesNames

def homeView(request):
    title = 'Our Universities (UJ/SU)'
    university_data = requests.get('https://api.covid19api.com/countries').json()
    return render(request,'dashboard.html',{'university_data':university_data, 'title':title})

class GetUniversityNames(TemplateView):
    template_name ='dashboard.html'   
    def get_context_data (self,*args, **kwargs):
        context= {'names':get_universitiesNames(),}  
        return context

class GetUniversityMarks(TemplateView):
    template_name ='dashboard.html'   
    def get_context_data (self,*args, **kwargs):
        context= {'marks':get_universitiesMarks(),}  
        return context