from django.urls import path
from . import views

app_name = 'api'

urlpatterns = [
    path('sign-up/', views.UserCreate.as_view()),
    path('authors/', views.api_authors_view, name='authors'),
    path('articles/', views.api_articles_view, name='articles'),
    path('articles/<slug>', views.api_article_slug_detail_view, name='detail'),
]