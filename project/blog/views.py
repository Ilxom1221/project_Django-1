from django.shortcuts import render, redirect
from .models import Category, Article
from .forms import ArticleForm
from  django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView


class ArticleListView(ListView):
    model = Article
    template_name = 'blog/index.html'
    context_object_name = 'articles'
    extra_context = {
        'title': 'PROWEB-Movies'
    }




class ArticleListByCategory(ArticleListView):

    def get_queryset(self):
        articles = Article.objects.filter(category_id=self.kwargs['pk'])
        return articles

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        category = Category.objects.get(pk=self.kwargs['pk'])
        context['title'] = f'{category.title}'
        return context




class ArticleDetailView(DetailView):
    model = Article
    context_object_name = 'article'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        article = Article.objects.get(pk=self.kwargs['pk'])
        context['title'] = f'{article.title}'
        return context






class NewArticle(CreateView):
    form_class = ArticleForm
    template_name = 'blog/add_category.html'
    extra_context = {
        'title': 'Добавить'
    }


