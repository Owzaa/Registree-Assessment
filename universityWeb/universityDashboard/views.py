from django.shortcuts import render
from django.views.generic import TemplateView
import requests




# GET__API then return University to JSON() DATA
def dashView(request):
    title = 'University - Dashboard'
    url = 'https://registree-coding-challenge.glitch.me/UJ/marks'
    response = requests.get(url,headers={'Authorization': 'Bearer %s' 'access_token'})
    university = response.json()
    university_marks = []
    university_names = []
    
    return render(request,'universityDashboard/template/dashboard.html',{'response': response, 'title':title,})

# Dashboard TableView
# security Authorization 
class DashboardTable(TemplateView):
    Template_name = 'universityDashboard/template/dashboard.html'
    def get_context_data (self,*args, **kwargs):
        pass  