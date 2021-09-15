# from JungleDevsProject.JungleDevs.api import serializer
from .models import Author
# from JungleDevsProject.JungleDevs import api
from rest_framework import viewsets, permissions, status
from .serializer import UserSerializer, AuthorSerializer, ArticleSerializer, ArticlePreviewSerializer
from .models import Author, Article
from rest_framework.response import Response
from rest_framework.decorators import action, api_view, permission_classes
# from django.contrib.auth.decorators import login_required


@api_view(['GET',])
def api_authors_view(request):
    try:
        authors = Author.objects.all()
    except Author.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = AuthorSerializer(authors, many=True)
        return Response(serializer.data)


@api_view(['GET',])
def api_articles_view(request):
    try:
        article = Article.objects.all()
    except Article.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ArticlePreviewSerializer(article, many=True)
        return Response(serializer.data)


@api_view(['GET',])
def api_article_slug_detail_view(request,slug):
    try:
        article = Article.objects.get(slug=slug)
    except Article.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ArticleSerializer(article)
        return Response(serializer.data)



#################################################################
# class UserViewSet(viewsets.ModelViewSet):
#     queryset = models.User.objects.all()
#     serializer_class = UserSerializer


# class AuthorViewSet(viewsets.ModelViewSet):
#     queryset = models.Author.objects.all()
#     serializer_class = AuthorSerializer
#     permission_classes = [permissions.IsAuthenticatedOrReadOnly]

#     def create(self, request):
#         serializer = AuthorSerializer(
#         data=request.data, context={'request': request})
#         serializer.is_valid(raise_exception=True) # check all fields is valid before attempting to save
#         serializer.save(user=request.user)
#         return Response(serializer.data)


# class ArticleViewSet(viewsets.ModelViewSet):
#     queryset = models.Article.objects.all()
#     serializer_class = ArticleSerializer
#     permission_classes = [permissions.IsAuthenticated]

#     def create(self, request):
#         serializer = ArticleSerializer(
#         data=request.data, context={'request': request})
#         serializer.is_valid(raise_exception=True) # check all fields is valid before attempting to save
#         serializer.save(user=request.user)
#         return Response(serializer.data)