from django.urls import path
from .views import *



urlpatterns = [
    path('', ArticleListView.as_view(), name='index'),
    path('category/<int:pk>', ArticleListByCategory.as_view(), name='category'),
    path('article/<int:pk>', ArticleDetailView.as_view(), name='article'),
    path('new/>', NewArticle.as_view(), name='views_category'),
]