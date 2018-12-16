from django.shortcuts import render
from django.views.generic import ListView, DetailView
from webapp.models import User, Article

# Create your views here.

class ArticleListView(ListView):
    model = Article
    template_name = 'article_list.html'

class UserListView(ListView):
    model = User
    template_name = 'user_list.html'

class ArticleDetailView(DetailView):
    model = Article
    template_name = 'article_detail.html'

class UserDetailView(DetailView):
    model = User
    template_name = 'user_detail.html'
