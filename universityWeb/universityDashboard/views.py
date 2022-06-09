from django.shortcuts import render
from django.views.generic import TemplateView
import requests


# API LINKS:
URL__API = ['https://registree-coding-challenge.glitch.me/UJ/marks',
            'https://registree-coding-challenge.glitch.me/UJ/names',
            'https://registree-coding-challenge.glitch.me/SU/marks',
            'https://registree-coding-challenge.glitch.me/su/names']


# GET__API then return University to JSON() DATA
def dashView(request):
    title = 'University - Dashboard'
    url = URL__API
    response = requests.get(url,headers={'Authorization': 'Bearer %s' 'access_token'})
    university = response.json()
    university_marks = []
    university_names = []
    for i in range(len(university['university'])):
        university_marks.append(university['university'][i])
        university_names.append(university['university'][i])
    return render(request,'universityDashboard/dashboard.html',{'response': response, 'title':title,'universities':universities})

# Dashboard TableView
class DashboardTable(TemplateView):
    Template_name = 'universityDashboard/dashboard.html'
    def get_context_data (self,*args, **kwargs):
        pass  