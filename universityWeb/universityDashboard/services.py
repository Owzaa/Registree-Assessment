import os
import requests

def get_universitiesMarks():
    url = "https://registree-coding-challenge.glitch.me/UJ/marks" or "https://registree-coding-challenge.glitch.me/SU/marks"
    response = requests.get(url,headers={'Authorization': 'Bearer %s' % os.getenv('DO_ACCESS_TOKEN')})
    university = response.json()
    university_marks = []

def get_universitiesNames():
    url = "https://registree-coding-challenge.glitch.me/UJ/names" or "https://registree-coding-challenge.glitch.me/SU/names"
    response = requests.get(url,headers={'Authorization': 'Bearer %s' % os.getenv('DO_ACCESS_TOKEN')})
    university = response.json()
    university_names = []