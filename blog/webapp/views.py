from django.shortcuts import render
from django.views.generic import ListView, DetailView, FormView, CreateView, UpdateView
from webapp.models import User, Article, Comment
from webapp.forms import SearchProjectForm, ArticleForm, CommentForm, CommentsForm
from django.urls import reverse_lazy, reverse

# Create your views here.

class ArticleListView(ListView, FormView):
    model = Article
    template_name = 'article_list.html'
    form_class = SearchProjectForm

    def get_queryset(self):
        article_name = self.request.GET.get('article_name')
        if article_name:
            return self.model.objects.filter(title__icontains=article_name) | self.model.objects.filter(text__icontains=article_name)
        else:
            return Article.objects.all()

class UserListView(ListView):
    model = User
    template_name = 'user_list.html'

class ArticleDetailView(DetailView):
    model = Article
    template_name = 'article_detail.html'

class UserDetailView(DetailView):
    model = User
    template_name = 'user_detail.html'

class ArticleCreateView(CreateView):
    model = Article
    form_class = ArticleForm
    template_name = 'article_create.html'
    success_url = reverse_lazy('article_list')

class CommentCreateView(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'comment_create.html'

    def get_success_url(self):
        return reverse('article_detail', kwargs={'pk': self.object.article.pk})


class ArticleUpdateView(UpdateView):
    model = Article
    form_class = ArticleForm
    template_name = 'article_update.html'

    def get_success_url(self):
        return reverse('article_detail', kwargs={'pk': self.object.pk})


class CommentUpdateView(UpdateView):
    model = Comment
    form_class = CommentsForm
    template_name = 'comment_update.html'

    def get_success_url(self):
        return reverse('article_detail', kwargs={'pk': self.object.article.pk})
