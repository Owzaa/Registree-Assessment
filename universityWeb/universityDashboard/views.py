from django.shortcuts import render
import requests


# API LINKS:
URL__API = ['https://registree-coding-challenge.glitch.me/UJ/marks',
            'https://registree-coding-challenge.glitch.me/UJ/names',
            'https://registree-coding-challenge.glitch.me/SU/marks',
            'https://registree-coding-challenge.glitch.me/su/names']


# GET__API then return University to JSON() DATA
def dashView(request,URL__API):
    title = 'University - Dashboard'
    response = requests.get(URL__API.json())
    def get_context_data (self,*args, **kwargs):
        pass  
    return render(request,'universityDashboard/dashboard.html',{'response': response, 'title':title})


