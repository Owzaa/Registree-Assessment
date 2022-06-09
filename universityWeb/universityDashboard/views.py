from django.shortcuts import render
from django.views.generic import TemplateView
import os
from .services import get_universitiesMarks, get_universitiesNames

def homeView(request):
    title = 'University - Dashboard'
    universityData =get_universitiesNames() 
    return render(request,'dashboard.html',{'universityData':universityData,'title':title})


class GetUniversityNames(TemplateView):
    Template_name ='dashboard.html'   
    def get_context_data (self,*args, **kwargs):
        context= {'names':get_universitiesNames(),}  
        return context

class GetUniversityMarks(TemplateView):
    Template_name ='dashboard.html'   
    def get_context_data (self,*args, **kwargs):
        context= {'marks':get_universitiesMarks(),}  
        return context