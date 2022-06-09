from django.shortcuts import render
from django.views.generic import TemplateView
import requests
import os
from .services import get_universitiesMarks,get_universitiesNames
from django.contrib.auth.decorators import login_required,permission_required

"""@permission_required('homeView',raise_exception=True)"""
def homeView(request):
    title = 'Our Universities (UJ/SU)'
    universities = GetUniversityMarks and GetUniversityNames
    return render(request,'dashboard.html',{'universities':universities, 'title':title})


class GetUniversityNames(TemplateView):
    def get_context_data (self,*args, **kwargs):
        context= ContentType.objects.GET.get_universitiesNames()
        return context

class GetUniversityMarks(TemplateView):
    def get_context_data (self,*args, **kwargs):
        context= get_universitiesMarks
        return context