from django.urls import path

from cbv_demos.web.views import list_articles, ArticlesListView, RedirectToArticlesView, ArticleDetailView, \
    ArticleCreateView

urlpatterns = [
    path('', list_articles, name='list articles'),
    path('cbv/', ArticlesListView.as_view(), name='list articles cbv'),
    path('cbv/<int:pk>/', ArticleDetailView.as_view(), name='details article'),
    path('cbv/create/', ArticleCreateView.as_view(), name='create article'),
    path('redirect-to-articles', RedirectToArticlesView.as_view(), name='redirect'),
]