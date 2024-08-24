from django.shortcuts import render
from requests import *

API_key = '5470dbb6be724001a28c4ec2fa26614c'
# Create your views here.
def search_category(request):
    search_query = 'главные новости'
    if request.method == 'POST':
        search_query = request.POST.get('search_query')
    return search_query
def homepage_view(request):
    news = get_news(search_category(request))
    #print(f'[!] NEWS: \n{news}')
    return render(request, "index.html", {'news_items': news})

def get_news(category):
    response = get(f'https://newsapi.org/v2/everything?q={category}'
                   f'&language=ru&apiKey={API_key}')
    data = response.json()
    if data['status'] != 'ok':
        return []
    return data['articles']