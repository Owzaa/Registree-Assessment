import os
import requests

def get_universitiesMarks():
    url = "https://registree-coding-challenge.glitch.me/UJ/marks" 
    response = requests.get(url,headers={'Authorization': 'Bearer %s' % os.getenv('DO_ACCESS_TOKEN')})
    universities  = response.json()
    university_marks = []
    for i in range(len(universities['universities'])):
        university_marks.append(universities['universities'][i])
    return university_marks

def get_universitiesNames():
    url = "https://registree-coding-challenge.glitch.me/UJ/names"
    r = requests.get(url,headers={'Authorization': 'Bearer %s' % os.getenv('DO_ACCESS_TOKEN')})
    universities = r.json()
    university_names = []
    for i in range(len(universities['universities'])):
        university_names.append(universities['universities'][i])
    return university_names


def get_universitiesMarks():
    url = "https://registree-coding-challenge.glitch.me/SU/marks"
    r = requests.get(url,headers={'Authorization': 'Bearer %s' % os.getenv('DO_ACCESS_TOKEN')})
    universities = r.json()
    university_marks = []
    for i in range(len(universities_marks['universities_marks'])):
        university_marks.append(universities_marks['universities_marks'][i])
    return university_marks


def get_universitiesNames():
    url = "https://registree-coding-challenge.glitch.me/SU/names"
    r = requests.get(url,headers={'Authorization': 'Bearer %s' % os.getenv('DO_ACCESS_TOKEN')})
    universities = r.json()
    university_names = []
    for i in range(len(universities['universities'])):
        university_names.append(universities['universities'][i])
    return university_names