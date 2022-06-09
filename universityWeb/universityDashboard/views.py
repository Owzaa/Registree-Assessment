from django.shortcuts import render
from django.views.generic import TemplateView
import requests
import os

class GetUniversityMarks(TemplateView):   
    url = 'https://registree-coding-challenge.glitch.me/UJ/marks' or 'https://registree-coding-challenge.glitch.me/SU/marks' 
    response = requests.get(url,headers={'Authorization': 'Bearer %s' % os.getenv('DO_ACCESS_TOKEN')})
    university = response.json()
    university_marks = []
    def get_context_data (self,*args, **kwargs):
        pass  

class GetUniversityNames(TemplateView):
    url = 'https://registree-coding-challenge.glitch.me/UJ/names' or 'https://registree-coding-challenge.glitch.me/SU/names' 
    response = requests.get(url,headers={'Authorization': 'Bearer %s' % os.getenv('DO_ACCESS_TOKEN')})
    university = response.json()
    university_names = []
    def get_context_data (self,*args, **kwargs):
        pass  
