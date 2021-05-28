import requests
from django.shortcuts import render




# Create your views here.
def index(request):
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


def Nview(request, name):
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
