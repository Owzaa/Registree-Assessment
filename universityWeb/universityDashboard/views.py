from django.shortcuts import render
from django.views.generic import TemplateView
import os
from .services import get_universitiesMarks, get_universitiesNames

def homeView(request):
    title = 'University - Dashboard'
    university_marks = get_universitiesMarks()
    university_names = get_universitiesNames()
    return render(request,'dashboard.html',{'university_marks':university_marks,
                                            'university_names':university_names,'title':title})

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