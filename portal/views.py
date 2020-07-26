from django.shortcuts import render
from twitterscraper import query_tweets
from datetime import date
from .models import Tweet, Article, Reference

import requests


def tweets_list(request):
  return render(request, 'portal/tweets_list.html', {'tweets': ['Realize uma busca para verificar os resultados!']})

def home(request):
  return render(request, 'portal/home.html')

def articles(request):
  articles = Article.objects.all()
  return render(request, 'portal/articles.html', {'articles': articles})

def portals(request):
  references = Reference.objects.all()
  return render(request, 'portal/portals.html', {'references': references})

def tweets_search(request):
  if request.method == 'POST':
    key_groups = []
    username = request.POST.get('username')
    word_group = request.POST.get('group').split('&')

    for group in word_group:
      key_groups.append(group.split(','))

    start_date = request.POST.get('startDate').split('-')
    end_date = request.POST.get('endDate').split('-')
    keywords = request.POST.get('words').split(',')

    begin_date = f'{start_date[2]}-{start_date[1]}-{start_date[0]}'
    end_date = f'{end_date[2]}-{end_date[1]}-{end_date[0]}'

    tweets = []
    for tweet in query_tweets(query=f"{query_constructor(keywords, key_groups)} from:{username}", limit=40, poolsize=1, begindate=date.fromisoformat(begin_date), enddate=date.fromisoformat(end_date)):
      tweets.append(tweet.text)
    return render(request, 'portal/tweets_list.html', {'tweets': tweets})
  else:
    return render(request, 'portal/tweets_search.html')

def query_constructor(exact_match = [], partial_match = []):
  query = ''
  for i in range(0, len(exact_match)):
    if (i != len(exact_match) - 1):
      query += '"' + exact_match[i] + '" OR '
    else:
      query += '"' + exact_match[i] + '" '

  if len(partial_match) > 0:
    query += 'OR '

  for i in range(0, len(partial_match)):
    query += '('
    for j in range(0, len(partial_match[i])):
      if (j != len(partial_match[i]) - 1):
        query += '"' + partial_match[i][j] + '" AND '
      else:
        query += '"' + partial_match[i][j] + '"'
    if (i != len(partial_match) - 1):
      query += ') OR '
    else:
      query += ') '

  return query