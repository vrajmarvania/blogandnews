import requests
from django.contrib import auth, messages
from django.shortcuts import render, redirect


# Create your views here.
def index(request):
    if request.session.has_key('ID'):
        print("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
        query_params = {
            "country": "in",
            "source": "CNN",
            "sortBy": "top",
            "apiKey": "57bacea1eac14b82bd851fcb8c72a30d"
        }
        main_url = " https://newsapi.org/v1/articles"

        # fetching data in json format
        res = requests.get(main_url, params=query_params)
        open_bbc_page = res.json()
        print(open_bbc_page)
        data = open_bbc_page.get('articles')
        params = {'data': data}
        return render(request, 'index.html', params)
    else:
        return render(request,'mysite/signup.html')




def Nview(request, name):
    if request.session.has_key('ID'):

        query_params = {
            "country":"in",
            "source": "CNN",
            "sortBy": "top",
            "apiKey": "57bacea1eac14b82bd851fcb8c72a30d"
        }
        main_url = " https://newsapi.org/v1/articles"

        # fetching data in json format
        res = requests.get(main_url, params=query_params)
        open_bbc_page = res.json()
        print(open_bbc_page)
        data = open_bbc_page.get('articles')
        for i in data:


            if (i.get("title")) == name:
                param = {'data': i}
                return render(request, 'Nview.html', param)
    else:
        return render(request,'mysite/signup.html')