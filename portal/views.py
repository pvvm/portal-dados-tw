from django.shortcuts import render
from .models import Tweet
# Create your views here.
def tweets_list(request):
  tweets = Tweet.objects.all()
  return render(request, 'portal/tweets_list.html', {'tweets': tweets})
