from django.shortcuts import render
from .models import Tweet
import requests
# Create your views here.
def tweets_list(request):
  # pokemons = requests.get('http://localhost:3333/')
  tweets = []
  # for tweet in pokemons.json():
  #   tweets.append(tweet['text'])
  return render(request, 'portal/tweets_list.html', {'tweets': tweets})

def home(request):
  return render(request, 'portal/home.html')

def articles(request):
  return render(request, 'portal/articles.html')

def portals(request):
  return render(request, 'portal/portals.html')

def tweets_search(request):
  return render(request, 'portal/tweets_search.html')
