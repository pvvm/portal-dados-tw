from django.shortcuts import render
from .models import Tweet, Article, Reference
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
  articles = Article.objects.all()
  return render(request, 'portal/articles.html', {'articles': articles})

def portals(request):
  references = Reference.objects.all()
  return render(request, 'portal/portals.html', {'references': references})

def tweets_search(request):
  return render(request, 'portal/tweets_search.html')
