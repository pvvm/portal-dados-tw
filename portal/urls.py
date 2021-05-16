from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('list', views.tweets_list, name='tweets_list'),
  path('search', views.tweets_search, name='tweets_search'),
  path('articles', views.articles, name='articles'),
  path('portals', views.portals, name='portals'),
  path('graphics', views.graphics, name='graphics'),
]