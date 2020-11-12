from django.shortcuts import render
from django.http import JsonResponse
import requests
from bs4 import BeautifulSoup

# Create your views here.


def index(request):
    pageurl = 'https://kathmandupost.com/covid19'
    page = requests.get(pageurl)
    soup = BeautifulSoup(page.content, 'html.parser')
    lis = []
    for tr in soup.find_all('tr'):
        lis.append([td.get_text() for td in tr.find_all('td')])

    lis.remove(lis[0])
    lis.remove(lis[0])

    return JsonResponse(lis, safe=False)
