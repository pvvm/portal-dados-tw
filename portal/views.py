from django.shortcuts import render
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
    form = []
    key_groups = []
    username = request.POST.get('username')
    key_groups_aux = request.POST.get('group').split('&')
    for group in key_groups_aux:
      key_groups.append(group.split(','))
    start_date = request.POST.get('startDate').split('-')
    end_date = request.POST.get('endDate').split('-')
    key_words = request.POST.get('words').split(',')
    query = f'username={username}&startDay={start_date[0]}&startMonth={start_date[1]}&startYear={start_date[2]}'
    query += f'&endDay={end_date[0]}&endMonth={end_date[1]}&endYear={end_date[2]}'
    query += f'&query={query_constructor(key_words, key_groups)}'
    response = requests.get(f'http://localhost:3333/?{query}')
    tweets = []
    for tweet in response.json():
      tweets.append(tweet['text'])
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