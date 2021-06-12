import requests
from django.contrib import auth, messages
from django.shortcuts import render, redirect


# Create your views here.
def index(request, s='vice-news'):
    if request.session.has_key('ID'):

        url = ('https://newsapi.org/v2/top-headlines?'
               'sources=' + s + '&'
                                'apiKey=8cbb433989614c04a8be7b697b277b06')

        response = requests.get(url)
        open_bbc_page = response.json()
        print(open_bbc_page)
        data = open_bbc_page.get('articles')
        print(data)
        params = {'data': data, 's': s}
        return render(request, 'index.html', params)
    else:
        return render(request, 'mysite/signup.html')


def Nview(request, s, name):
    if request.session.has_key('ID'):

        url = ('https://newsapi.org/v2/top-headlines?'
               'sources=' + s + '&'
                                'apiKey=8cbb433989614c04a8be7b697b277b06')

        response = requests.get(url)
        open_bbc_page = response.json()
        data = open_bbc_page.get('articles')
        for i in data:
            if (i.get("title")) == name:
                param = {'data': i}
                return render(request, 'Nview.html', param)
    else:
        return render(request, 'mysite/signup.html')
